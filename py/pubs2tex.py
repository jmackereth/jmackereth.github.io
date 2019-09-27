from datetime import date
import json
import re
from utf8totex import utf8totex

#Stolen shamelessly and adapted from Adrien Price-Whelan
#(under creative commons licence https://creativecommons.org/licenses/by/4.0/)
# Added functionality to isolate conference proceedings, and output co-authored publications into separate lists
#original version https://github.com/adrn/cv

_JOURNAL_MAP = {
    "ArXiv e-prints": "ArXiv",
    "The Astronomical Journal": "\\aj",
    "The Astrophysical Journal": "\\apj",
    "The Astrophysical Journal Supplement Series": "\\apjs",
    "Astronomy and Astrophysics": "\\aanda",
    "Galaxies": "MDPI: galaxies",
    "The Journal of Open Source Software": "JOSS",
    "Monthly Notices of the Royal Astronomical Society": "\\mnras",
    "Nature": "\\nature",
    "Nature Astronomy": "\\natureast",
    "Publications of the Astronomical Society of the Pacific": "\\pasp",
    "Publications of the Astronomical Society of Japan": "\\pasj",
}

JOURNAL_SKIP = [
    "VizieR Online Data Catalog",
    "^American Astronomical Society.*",
    "^AAS.*",
    "Astrophysics Source Code Library",
    "Zenodo Software Release",
    "Ph.D. Thesis",
    "Spitzer Proposal",
    "The Astronomer's Telegram",
]
JOURNAL_SKIP = [x.lower() for x in JOURNAL_SKIP]


# Lower case journals:
JOURNAL_MAP = {}
for k, v in _JOURNAL_MAP.items():
    JOURNAL_MAP[k.lower()] = v


def format_name(name):
    try:
        last, others = name.split(', ')
        others = ['{0}.'.format(o[0]) for o in others.split()]
        name = "{last}, {first}".format(first=' '.join(others), last=last)

    except ValueError:
        print("couldn't format name '{0}'".format(name))

    return name


def parse_authors(paper_dict, max_authors=4):
    raw_authors = [utf8totex(x) for x in paper_dict['authors']]

    show_authors = raw_authors[:max_authors]

    if any(['mackereth' in x.lower() for x in show_authors]):
        # Bold my name because it makes the cut to be shown
        names = []
        for name in show_authors:
            if 'mackereth' in name.lower():
                name = '\\textbf{Mackereth,~J.~T.}'
            else:
                name = format_name(name)
            names.append(name)

        author_tex = '; '.join(names)

        if len(show_authors) < len(raw_authors): # use et al.
            author_tex = author_tex + "~et al."

    else:
        # Add "incl. " after et al., because I'm buried in the author list
        author_tex = "{0}".format(format_name(show_authors[0]))
        author_tex += "~et al.~(incl. \\textbf{JTM})"

    return author_tex


def filter_papers(pubs):
    filtered = []

    for p in pubs:
        if p["pub"] is None:
            continue

        # Skip if the publication is in the skip list:
        if any([re.match(re.compile(pattr), p['pub'].lower())
                for pattr in JOURNAL_SKIP]):
            continue

        if p["pub"].lower() != "arxiv e-prints":
            pub = JOURNAL_MAP.get(p["pub"].strip("0123456789# ").lower(),
                                  None)

            if pub is None:
                if p['doctype'] == "inproceedings":
                    pub = p['pub']
                else:
                    print("Journal '{0}' not recognized for paper '{1}' - "
                          " skipping...".format(p['pub'], p['title']))
                    continue

        # HACK: hard-coded skip
        if 'astropy problem' in p['title'].lower():
            continue

        filtered.append(p)

    return filtered



def get_paper_items(papers):
    refereeds = []
    proceedings = []
    preprints = []
    first_authors = []
    co_authors = []
    for paper in papers:
        authors = parse_authors(paper)
        entry = authors

        # Skip if the publication is in the skip list:
        if any([re.match(re.compile(pattr), paper['pub'].lower())
                for pattr in JOURNAL_SKIP]):
            continue

        is_proceedings = False
        if paper['doctype'] == 'inproceedings':
            is_proceedings = True

        if paper["doi"] is not None:
            title = "\\doi{{{0}}}{{{1}}}".format(paper["doi"],
                                                 utf8totex(paper["title"]))
        else:
            title = "\\textit{{{0}}}".format(utf8totex(paper["title"]))
        entry += ", " + title

        if paper['pubdate'] is not None:
            entry += ", {0}".format(paper['pubdate'].split('-')[0])

        if paper["pub"] not in [None, "ArXiv e-prints", "arXiv e-prints"]: # HACK
            pub = JOURNAL_MAP.get(paper["pub"].strip("0123456789# ").lower(),
                                  None)

            if pub is None:
                if is_proceedings:
                    pub = paper['pub']
                else:
                    print("Journal '{0}' not recognized for paper '{1}' - "
                          " skipping...".format(paper['pub'], paper['title']))
                    continue

            entry += ", " + pub
            is_preprint = False

        else:
            is_preprint = True

        if is_proceedings:
            print(is_preprint)

        if paper["volume"] is not None:
            entry += ", {{{0}}}".format(paper["volume"])

        if paper["page"] is not None:
            entry += ", {0}".format(paper["page"])

        if paper["arxiv"] is not None:
            entry += " (\\arxiv{{{0}}})".format(paper["arxiv"])

        #if paper["citations"] > 1:
            #entry += (" [\\href{{{0}}}{{{1} citations}}]"
                     # .format(paper["url"], paper["citations"]))

        if is_preprint:
            preprints.append(entry)
        elif is_proceedings:
            proceedings.append(entry)
        else:
            refereeds.append(entry)

        if "mackereth" in paper["authors"][0].lower() and not is_proceedings:
            first_authors.append(entry)

        if "mackereth" not in paper["authors"][0].lower() and not is_proceedings:
            co_authors.append(entry)

    # Now go through and add the \item and numbers:
    for corpus in [preprints, proceedings, refereeds, first_authors, co_authors]:
        for i, item in enumerate(corpus):
            num = len(corpus) - i
            corpus[i] = ("\\item[{\\scriptsize" +
                         str(num) + "}]" + item)

    return refereeds, proceedings, preprints, first_authors, co_authors


if __name__ == '__main__':
    from os import path
    if not path.exists('pubs.json'):
        raise FileNotFoundError("File 'pubs.json' not found - run get_pubs.py "
                                "before running this script.")

    with open("pubs.json", "r") as f:
        pubs = json.loads(f.read())

    papers = filter_papers(pubs)
    refs, procs, unrefs, first, coauth = get_paper_items(papers)

    # Compute citation stats
    nref = len(refs)
    nfirst = sum(1 for p in papers if "Mackereth" in p["authors"][0])
    cites = sorted((p["citations"] for p in papers), reverse=True)
    ncitations = sum(cites)
    hindex = sum(c >= i for i, c in enumerate(cites))

    summary = (("refereed: {1} --- first author: {2} --- citations: {3} --- "
               "h-index: {4} (\\textit{{{0}}})")
               .format(date.today(), nref, nfirst, ncitations, hindex))

    print("-"*32)
    print("Summary:")
    print(summary)

    with open("../cv/summary.tex", "w") as f:
        f.write(summary)

    with open("../cv/pubs_ref.tex", "w") as f:
        f.write("\n\n".join(refs))

    with open("../cv/pubs_unref.tex", "w") as f:
        f.write("\n\n".join(unrefs))

    with open("../cv/pubs_firstauthor.tex", "w") as f:
        f.write("\n\n".join(first))

    with open("../cv/pubs_coauthor.tex", "w") as f:
        f.write("\n\n".join(coauth))

    with open("../cv/pubs_proceedings.tex", "w") as f:
        f.write("\n\n".join(procs))
