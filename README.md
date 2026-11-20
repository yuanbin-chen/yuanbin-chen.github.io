# Yuanbin Chen · Academic Homepage

Jekyll site for `https://yuanbin-chen.github.io/`, adapted from [Shaoyan Liu’s Academic Homepage](https://github.com/shaoyanliu/academic-homepage). See `THIRD_PARTY_NOTICES.md` for upstream and bundled library credits.

## Update the site

| Content | Location |
| --- | --- |
| Name, affiliation, email, profiles, portrait, and CV path | `_config.yml` |
| Homepage introduction and links to research interests | `index.md` and `_data/research_interests.yml` |
| Full biography | `bio.md` |
| Homepage news and the News page | `_data/news.yml` |
| Research descriptions and figures | `research.md` and `assets/img/` |
| Papers, featured papers, and topics | `_data/publications.yml`, `_data/publication_topics.yml`, and `bib/` |
| Honors, academic services, and research projects | `honors.md`, `services.md`, and `projects.md` |
| Public CV and PDF reader headings | `cv/yuanbin-chen-cv.pdf` and `_data/cv_sections.yml` |

A paper appears on the homepage when its record has `selected: true`. Use `image`, `image_alt`, and `summary` for its homepage illustration and description. Each publication `id` also serves as its page anchor. Set `author_role` to `first`, `co-first`, or `coauthor`. The first-author list includes papers with shared first authorship. The CV is a public copy with personal phone numbers and citizenship removed. Use a public copy when replacing it.

Add news items at the top of `_data/news.yml` using `month: "YYYY-MM"` and a title. The description, link, link label, and submission deadline are optional. The homepage shows the first three items and the News page lists all items.

## Preview with Jekyll

Install Ruby and Bundler. From this directory, run:

```sh
bundle install
bundle exec jekyll serve
```

Open `http://localhost:4000/`. The HTTP preview supports the embedded PDF reader and the BibTeX dialog.

## GitHub Pages

The included GitHub Actions workflow builds the default branch. After reviewing the preview, install the source in the existing personal site repository. In **Settings → Pages → Build and deployment**, select **GitHub Actions**. The root-domain configuration uses an empty `baseurl` and retains the main `/publications/` and `/cv/` routes.
