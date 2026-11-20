{% include scholar-snapshot.html %}
{% assign publication_data = site.data.publications %}
{% assign papers = site.papers | sort: 'order', 'last' %}
{% if include.selected_only %}
<h2 id="selected-publications" class="selected-publications-heading"><a href="{{ '/publications/' | relative_url }}">{{ site.data.home.featured_heading | escape }}</a></h2>
{% else %}
<h1 id="publications" class="page-title">{{ publication_data.heading | escape }}</h1>

<div class="publication-profiles" role="group" aria-label="Publication profiles">
  {% if site.data.profile.google_scholar and site.data.profile.google_scholar != '' %}<a href="{{ site.data.profile.google_scholar | escape }}">Google Scholar</a>{% endif %}
  {% if site.data.profile.researchgate and site.data.profile.researchgate != '' %}<a href="{{ site.data.profile.researchgate | escape }}">ResearchGate</a>{% endif %}
</div>
{% endif %}

<div class="publications{% if include.selected_only %} selected-publications{% endif %}" data-publication-list>
{% if include.selected_only %}
  {% assign selected_papers = papers | where: "selected", true %}
  {% include publication-list.html papers=selected_papers featured=true %}
{% else %}
  {% assign first_author_papers = papers | where_exp: "paper", "paper.author_role != 'coauthor'" %}
  {% assign paper_years = first_author_papers | group_by: 'year' | sort: 'name' | reverse %}
  {% assign newest_first = '' | split: ',' %}
  {% for year in paper_years %}
    {% assign newest_first = newest_first | concat: year.items %}
  {% endfor %}
  {% assign journals = newest_first | where_exp: "paper", "paper.publication_type != 'conference'" %}
  {% assign conferences = newest_first | where: "publication_type", "conference" %}
  {% assign other_papers = papers | where: "author_role", "coauthor" %}
  <section class="publication-group" aria-labelledby="first-author-publications" data-publication-group>
    <h2 id="first-author-publications">{{ publication_data.first_heading | escape }}</h2>
    {% if journals.size > 0 %}
    <h3 id="journal-papers" class="publication-type-heading">{{ publication_data.journal_heading | escape }}</h3>
    {% include publication-list.html papers=journals numbered=true number_prefix="J" %}
    {% endif %}
    {% if conferences.size > 0 %}
    <h3 id="conference-papers" class="publication-type-heading">{{ publication_data.conference_heading | escape }}</h3>
    {% include publication-list.html papers=conferences numbered=true number_prefix="C" %}
    {% endif %}
  </section>
  <section class="publication-group" aria-labelledby="non-first-author-publications" data-publication-group>
    <h2 id="non-first-author-publications">{{ publication_data.other_heading | escape }}</h2>
    {% include publication-list.html papers=other_papers numbered=true %}
  </section>
{% endif %}
</div>
{% if include.selected_only %}
<p class="selected-publications-all"><a href="{{ '/publications/' | relative_url }}">{{ site.data.home.featured_link_label | escape }}</a></p>
{% endif %}

<dialog class="publication-bibtex-dialog" id="publication-bibtex-dialog" aria-labelledby="bibtex-dialog-title" aria-describedby="bibtex-paper-title">
  <div class="bibtex-dialog-heading">
    <h2 id="bibtex-dialog-title">BibTeX</h2>
    <button type="button" class="bibtex-close" data-bibtex-close aria-label="Close citation">&times;</button>
  </div>
  <p class="bibtex-paper-title" id="bibtex-paper-title" data-bibtex-title></p>
  <pre class="bibtex-content" data-bibtex-content tabindex="0" aria-label="BibTeX citation"></pre>
  <p class="bibtex-status" data-bibtex-status role="status" aria-live="polite"></p>
  <div class="bibtex-dialog-actions">
    <button type="button" data-bibtex-copy disabled>Copy BibTeX</button>
    <a data-bibtex-download download>Download .bib</a>
  </div>
</dialog>
<script src="{{ '/assets/js/publications.js' | relative_url }}?v={{ site.time | date: '%s' }}" defer></script>
