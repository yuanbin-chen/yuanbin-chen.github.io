---
layout: default
title: CV
editorial: cv_sections
permalink: /cv/
full_width: true
cv_reader: true
---

<div class="cv-heading">
  <h1>{{ site.data.cv_sections.heading | escape }}</h1>
  <a class="cv-download" href="{{ site.data.profile.cv_pdf | relative_url }}" download="{{ site.data.profile.title | slugify }}-cv.pdf" aria-label="Download {{ site.data.profile.title | escape }}'s CV (PDF)" title="Download CV (PDF)">
    <i class="fa-solid fa-file-pdf" aria-hidden="true"></i>
  </a>
</div>



<a class="cv-view-link" href="{{ site.data.profile.cv_pdf | relative_url }}" target="_blank" rel="noopener noreferrer">View PDF</a>

<div class="cv-reader" data-pdf-url="{{ site.data.profile.cv_pdf | relative_url }}" aria-label="CV PDF reader">
  <div class="cv-toolbar" hidden>
    <span class="cv-page-count"><span data-cv-total>–</span> pages</span>
    <span class="cv-toolbar-divider" aria-hidden="true"></span>
    <button type="button" data-cv-action="out" aria-label="Zoom out">−</button>
    <button type="button" data-cv-action="fit">Fit width</button>
    <button type="button" data-cv-action="in" aria-label="Zoom in">+</button>
  </div>
  <p class="cv-reader-status" role="status">Loading PDF…</p>
  <div class="cv-reader-body">
    <button class="cv-sections-toggle" type="button" aria-expanded="false" aria-controls="cv-sections" hidden><i class="fa-solid fa-list" aria-hidden="true"></i> Sections</button>
    <nav id="cv-sections" class="cv-sections-panel" aria-label="CV sections" hidden>
      {% for item in site.data.cv_sections.sections %}
      <button type="button" data-cv-heading="{{ item.heading | escape }}" hidden>{{ item.title | escape }}</button>
      {% endfor %}
    </nav>
    <div class="cv-page-viewport" role="region" aria-label="CV pages, scroll to read" tabindex="0" hidden></div>
  </div>
  <noscript><p>Please use View PDF above to read the CV.</p></noscript>
</div>
<script type="module" src="{{ '/assets/js/cv.js' | relative_url }}?v={{ site.time | date: '%s' }}"></script>
