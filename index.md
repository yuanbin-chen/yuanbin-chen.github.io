---
layout: homepage
title: Home
---

{% assign home = site.data.home %}
<div class="academic-profile">
  <div class="academic-profile-copy">
    <h1 id="about-me">{{ site.data.profile.title | escape }}{% if site.data.profile.name_zh and site.data.profile.name_zh != '' %} <span lang="zh">{{ site.data.profile.name_zh | escape }}</span>{% endif %}</h1>
    <p class="academic-affiliation">{% if site.data.profile.affiliation_link and site.data.profile.affiliation_link != '' %}<a href="{{ site.data.profile.affiliation_link | escape }}">{{ site.data.profile.affiliation | escape }}</a>{% else %}{{ site.data.profile.affiliation | escape }}{% endif %}</p>
    <div class="academic-bio">
      {{ home.introduction | markdownify }}
    </div>
    {% if site.data.research.topics.size > 0 %}
    <p class="academic-bio">
      {{ home.interests_intro | escape }}
      {% for topic in site.data.research.topics -%}
        <a href="{{ '/research/#' | append: topic.id | relative_url | escape }}">{{ topic.title | escape }}</a>{% if forloop.last %}.{% elsif forloop.rindex == 2 %}, and {% else %}, {% endif %}
      {%- endfor %}
    </p>
    {% endif %}
    <div class="academic-profile-links" role="group" aria-label="Academic profiles">
      {% if site.data.profile.google_scholar and site.data.profile.google_scholar != '' %}<a href="{{ site.data.profile.google_scholar | escape }}">Google Scholar</a>{% endif %}
      {% if site.data.profile.researchgate and site.data.profile.researchgate != '' %}<a href="{{ site.data.profile.researchgate | escape }}">ResearchGate</a>{% endif %}
      {% if site.data.profile.orcid and site.data.profile.orcid != '' %}<a href="{{ site.data.profile.orcid | escape }}">ORCID</a>{% endif %}
    </div>
    <div class="academic-profile-links academic-email-links" role="group" aria-label="Email addresses">
      {% if site.data.profile.email and site.data.profile.email != '' %}<a href="mailto:{{ site.data.profile.email | escape }}">{{ site.data.profile.email | escape }}</a>{% endif %}
      {% if site.data.profile.email2 and site.data.profile.email2 != '' %}<a href="mailto:{{ site.data.profile.email2 | escape }}">{{ site.data.profile.email2 | escape }}</a>{% endif %}
    </div>
  </div>
  {% if site.data.profile.avatar and site.data.profile.avatar != '' %}
  <figure class="academic-portrait">
    <img src="{{ site.data.profile.avatar | relative_url | escape }}" alt="{{ site.data.profile.title | escape }}" width="480" height="560" fetchpriority="high">
  </figure>
  {% endif %}
</div>

{% include news.md %}

{% include publications.md selected_only=true %}
