"""Update the counts and category filters in Pages CMS from the paper records."""

from pathlib import Path
import re
from textwrap import indent

import yaml

from sync_research_links import load_entries


CONFIG = Path(".pages.yml")
START = "    # BEGIN GENERATED PAPER VIEWS\n"
END = "    # END GENERATED PAPER VIEWS\n"
CATEGORIES = {
    "first_author_journals": "First-Author Journals",
    "first_author_conferences": "First-Author Conferences",
    "coauthor_papers": "Co-Author Papers",
}


def category(paper):
    if paper.get("author_role") == "coauthor":
        return "coauthor_papers"
    if paper.get("publication_type") == "conference":
        return "first_author_conferences"
    return "first_author_journals"


def main():
    papers = {
        Path(path).name: category(data)
        for path, (data, _) in load_entries("_papers").items()
    }
    original = CONFIG.read_text(encoding="utf-8")
    before, start, tail = original.partition(START)
    _, end, after = tail.partition(END)
    if not start or not end:
        raise ValueError("Missing the generated CMS paper view markers.")

    before, replacements = re.subn(
        r"(^    - name: papers\n      label: )All Papers \(\d+\)$",
        rf"\g<1>All Papers ({len(papers)})",
        before,
        flags=re.MULTILINE,
    )
    if replacements != 1:
        raise ValueError("Expected one All Papers collection label.")

    views = []
    for name, label in CATEGORIES.items():
        excluded = sorted(filename for filename, group in papers.items() if group != name)
        count = len(papers) - len(excluded)
        views.append(f"""    - name: {name}
      label: {label} ({count})
      type: collection
      path: _papers
      filename: *papers_filename
      format: yaml-frontmatter
      subfolders: false
      operations: *papers_operations
      view: *papers_view
      fields: *papers_fields
""")
        views.append(indent(yaml.safe_dump({"exclude": excluded}, allow_unicode=True), "      "))

    updated = before + start + "".join(views) + end + after
    if updated != original:
        CONFIG.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    main()
