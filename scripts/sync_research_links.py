"""Reconcile the research-topic and paper references edited in Pages CMS."""

from collections import defaultdict
import json
from pathlib import Path

import yaml


STATE_FILE = Path("scripts/research-publication-links.json")


def load_entries(folder):
    entries = {}
    for path in sorted(Path(folder).glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if not text.endswith("\n"):
            text += "\n"
        frontmatter, separator, body = text.removeprefix("---\n").partition("\n---\n")
        if not text.startswith("---\n") or not separator:
            raise ValueError(f"Missing YAML front matter in {path}")
        entries[path.as_posix()] = (yaml.safe_load(frontmatter), body)
    return entries


def write_links(entries, field, expected):
    for path, (data, body) in entries.items():
        previous = data.get(field) or []
        wanted = expected[path]
        # Keep each editor's existing display order. Append any reciprocal links.
        ordered = list(dict.fromkeys(ref for ref in previous if ref in wanted))
        ordered.extend(sorted(wanted.difference(ordered)))
        if ordered == previous:
            continue
        if ordered:
            data[field] = ordered
        else:
            data.pop(field, None)
        frontmatter = yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=105)
        Path(path).write_text(f"---\n{frontmatter}---\n{body}", encoding="utf-8")


def main():
    papers = load_entries("_papers")
    topics = load_entries("_research_topics")
    before = {tuple(link) for link in json.loads(STATE_FILE.read_text(encoding="utf-8"))}
    from_papers = {
        (topic, paper)
        for paper, (data, _) in papers.items()
        for topic in data.get("topics") or []
        if topic in topics
    }
    from_topics = {
        (topic, paper)
        for topic, (data, _) in topics.items()
        for paper in data.get("related_papers") or []
        if paper in papers
    }

    # An existing link is removed if either side removed it. A new link can be
    # introduced by either side. The checkpoint distinguishes these two edits.
    links = (from_papers & from_topics) | ((from_papers | from_topics) - before)
    expected_papers = defaultdict(set)
    expected_topics = defaultdict(set)
    for topic, paper in links:
        expected_papers[topic].add(paper)
        expected_topics[paper].add(topic)

    write_links(topics, "related_papers", expected_papers)
    write_links(papers, "topics", expected_topics)
    if links != before:
        STATE_FILE.write_text(json.dumps(sorted(links), indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
