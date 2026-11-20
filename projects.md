---
layout: default
title: Project
editorial: projects
permalink: /projects/
full_width: true
---

{% assign projects = site.data.projects %}
<h1 id="research-projects">{{ projects.heading | escape }}</h1>

{% for project in projects.items %}
<article class="project-entry">
  <h2>{{ project.title | escape }}</h2>
  {% if project.role or project.dates %}
  <p class="project-meta">{{ project.role | escape }}{% if project.role and project.dates %} · {% endif %}{{ project.dates | escape }}</p>
  {% endif %}
  {{ project.description | markdownify }}
  {% if project.link_url and project.link_url != '' %}
  <p><a href="{{ project.link_url | relative_url | escape }}">{{ project.link_label | default: 'Project details' | escape }}</a></p>
  {% endif %}
</article>
{% endfor %}
