---
layout: homepage
title: Home
---

{% assign home = site.data.home %}
{% assign profile = site.data.profile %}
<div class="academic-profile">
  <div class="academic-profile-copy">
    <h1 id="about-me">{{ profile.title | escape }}{% if profile.name_zh and profile.name_zh != '' %} <span lang="zh">{{ profile.name_zh | escape }}</span>{% endif %}</h1>
    <div class="academic-profile-meta">
      {% if profile.position or profile.affiliation %}
      <p>
        {{ profile.position | escape }}
        {%- if profile.affiliation and profile.affiliation != '' -%}
          {%- if profile.position and profile.position != '' %} at {% endif -%}
          {%- if profile.affiliation_link and profile.affiliation_link != '' -%}
            <a href="{{ profile.affiliation_link | escape }}">{{ profile.affiliation | escape }}</a>
          {%- else -%}
            {{ profile.affiliation | escape }}
          {%- endif -%}
        {%- endif %}
      </p>
      {% endif %}
      {% if home.distinction and home.distinction != '' %}
      <p>{{ home.distinction | escape }}</p>
      {% endif %}
    </div>
    <div class="academic-bio">
      {{ home.introduction | markdownify }}
    </div>
    {% if home.research_interests.size > 0 %}
    <div class="academic-bio academic-interests">
      <p>{{ home.interests_intro | escape }}</p>
      <ul>
        {% for interest in home.research_interests %}
        <li>
          {%- if interest.url and interest.url != '' -%}
            <a href="{{ interest.url | relative_url | escape }}">{{ interest.title | escape }}</a>
          {%- else -%}
            {{ interest.title | escape }}
          {%- endif -%}
          {%- if interest.detail and interest.detail != '' %} ({{ interest.detail | escape }}){% endif -%}
        </li>
        {% endfor %}
      </ul>
    </div>
    {% endif %}
    <div class="academic-profile-links" role="group" aria-label="Contact and academic profiles">
      {% if profile.google_scholar and profile.google_scholar != '' %}<a href="{{ profile.google_scholar | escape }}">Google Scholar</a>{% endif %}
      {% if profile.researchgate and profile.researchgate != '' %}<a href="{{ profile.researchgate | escape }}">ResearchGate</a>{% endif %}
      {% if profile.orcid and profile.orcid != '' %}<a href="{{ profile.orcid | escape }}">ORCID</a>{% endif %}
      {% if profile.email and profile.email != '' %}<a href="mailto:{{ profile.email | escape }}">{{ profile.email | escape }}</a>{% endif %}
      {% if profile.email2 and profile.email2 != '' %}<a href="mailto:{{ profile.email2 | escape }}">{{ profile.email2 | escape }}</a>{% endif %}
    </div>
  </div>
  {% if profile.avatar and profile.avatar != '' %}
  <figure class="academic-portrait">
    <img src="{{ profile.avatar | relative_url | escape }}" alt="{{ profile.title | escape }}" width="480" height="560" fetchpriority="high">
  </figure>
  {% endif %}
</div>

{% include news.md %}

{% include publications.md selected_only=true %}
