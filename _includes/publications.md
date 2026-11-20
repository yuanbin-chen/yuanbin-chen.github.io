{% include scholar-snapshot.html %}
{% if include.selected_only %}
<h2 id="selected-publications" class="selected-publications-heading"><a href="{{ '/publications/' | relative_url }}">Selected Publications</a></h2>
{% else %}
<h1 id="publications" class="page-title">Publications</h1>

<div class="publication-profiles" role="group" aria-label="Publication profiles">
  {% if site.google_scholar %}<a href="{{ site.google_scholar | escape }}">Google Scholar</a>{% endif %}
  {% if site.researchgate %}<a href="{{ site.researchgate | escape }}">ResearchGate</a>{% endif %}
</div>
{% endif %}

<div class="publications{% if include.selected_only %} selected-publications{% endif %}" data-publication-list>
{% if include.selected_only %}
  {% assign selected_papers = site.data.publications.main | where: "selected", true %}
  {% include publication-list.html papers=selected_papers featured=true %}
{% else %}
  {% assign first_author_papers = site.data.publications.main | where_exp: "paper", "paper.author_role != 'coauthor'" %}
  {% assign other_papers = site.data.publications.main | where: "author_role", "coauthor" %}
  <section class="publication-group" aria-labelledby="first-author-publications" data-publication-group>
    <h2 id="first-author-publications">First-Author Publications</h2>
    {% include publication-list.html papers=first_author_papers numbered=true %}
  </section>
  <section class="publication-group" aria-labelledby="non-first-author-publications" data-publication-group>
    <h2 id="non-first-author-publications">Non-First-Author Publications</h2>
    {% include publication-list.html papers=other_papers numbered=true %}
  </section>
{% endif %}
</div>
{% if include.selected_only %}
<p class="selected-publications-all"><a href="{{ '/publications/' | relative_url }}">View all publications</a></p>
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
