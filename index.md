---
layout: homepage
title: Home
seo_title: Yuanbin Chen | Nanyang Technological University
---

<div class="academic-profile">
  <div class="academic-profile-copy">
    <h1 id="about-me">Yuanbin Chen <span lang="zh">陈源彬</span></h1>
    <p class="academic-affiliation"><a href="{{ site.affiliation_link }}">School of Electrical and Electronic Engineering</a></p>
    <p class="academic-bio">
      I am a Postdoctoral Research Fellow at Nanyang Technological University (NTU), Singapore, supervised by
      <a href="https://blogs.ntu.edu.sg/chau-yuen/">Prof. Chau Yuen</a>.
      I received my Ph.D. from Beijing University of Posts and Telecommunications in 2024 and my undergraduate degree from Beijing Jiaotong University in 2019.
    </p>
    <p class="academic-bio">
      My research interests include
      {% for interest in site.data.research_interests -%}
        <a href="{{ interest.url | relative_url }}">{{ interest.title | escape }}</a>{% if forloop.last %}.{% elsif forloop.rindex == 2 %}, and {% else %}, {% endif %}
      {%- endfor %}
    </p>
    <div class="academic-profile-links" role="group" aria-label="Academic profiles">
      <a href="{{ site.google_scholar }}">Google Scholar</a>
      <a href="{{ site.researchgate }}">ResearchGate</a>
      <a href="{{ site.orcid }}">ORCID</a>
    </div>
    <div class="academic-profile-links academic-email-links" role="group" aria-label="Email addresses">
      <a href="mailto:{{ site.email }}">{{ site.email }}</a>
      <a href="mailto:{{ site.email2 }}">{{ site.email2 }}</a>
    </div>
  </div>
  <figure class="academic-portrait">
    <img src="{{ site.avatar | relative_url }}" alt="Yuanbin Chen" width="480" height="560" fetchpriority="high">
  </figure>
</div>

{% include news.md %}

{% include publications.md selected_only=true %}
