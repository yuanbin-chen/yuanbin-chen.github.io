# Yuanbin Chen · Academic Homepage

Jekyll site for [yuanbin-chen.github.io](https://yuanbin-chen.github.io/), adapted from [Shaoyan Liu’s Academic Homepage](https://github.com/shaoyanliu/academic-homepage). See `THIRD_PARTY_NOTICES.md` for upstream and bundled library credits.

## Edit content with Pages CMS

1. Sign in to [Pages CMS](https://app.pagescms.org/) with GitHub.
2. Install Pages CMS for the `yuanbin-chen/yuanbin-chen.github.io` repository. Open that repository and select its `master` branch.
3. Select a form, make your changes, and save. GitHub Pages deploys each saved change through the repository’s Actions workflow.

| Form | Content | Source |
| --- | --- | --- |
| Profile and contact | Name, university, portrait, emails, profiles, position, and public CV PDF | `_data/profile.yml` |
| Home | Introduction, honor below the university line, research interests, and news display | `_data/home.yml` |
| Bio | Full biography and education | `_data/bio.yml` |
| Research | Research topics, related papers, and figures | `_research_topics/` |
| Publications | Papers, author roles, research links, BibTeX, and homepage selections | `_papers/` |
| Projects | Project names, roles, dates, descriptions, and links | `_data/projects.yml` |
| Honors | Awards and dates | `_data/honors.yml` |
| Professional services | Editorial and conference service | `_data/services.yml` |
| News | Announcements, deadlines, and links | `_data/news.yml` |
| Navigation | Top menu labels, order, and links | `_data/navigation.yml` |
| CV reader | CV page heading and PDF section bookmarks | `_data/cv_sections.yml` |

- Edit the short research interests list in **Home** and the detailed topic sections in **Research**. There is one list of news items, sorted by month. The homepage shows the latest items up to the count set in Home.
- In Publications, select **First author**, **Co-first author**, or **Non-first author**. Set **Publication type** to Journal paper or Conference paper. First-author and co-first-author papers are grouped by type and sorted by year, newest first. Set **Display order** to arrange papers from the same year. Enable **Show on the homepage** and add a figure and summary for a selected publication. The saved file name supplies the paper's link ID.
- Select related papers in **Research → Topics** or research topics in **Publications → Papers**. Either editor can add or remove a link. The deployment workflow copies the change to the other editor and updates both public pages. Refresh the editor after the deployment finishes.
- Use **Images** to upload a portrait or figure. Upload a public copy of the CV under **CV PDFs**, then select the file in **Profile and contact**. Set section bookmarks in **CV reader** if the PDF headings have changed.

## Preview with Jekyll

Install Ruby and Bundler. From this directory, run:

```sh
bundle install
bundle exec jekyll serve
```

Open `http://localhost:4000/`. The HTTP preview supports the embedded PDF reader and the BibTeX dialog.

## GitHub Pages

The included GitHub Actions workflow builds the default branch. In **Settings → Pages → Build and deployment**, select **GitHub Actions**. The root-domain configuration uses an empty `baseurl`.
