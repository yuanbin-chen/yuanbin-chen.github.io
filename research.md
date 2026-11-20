---
layout: default
title: Research
editorial: research
permalink: /research/
full_width: true
---

{% assign research = site.data.research %}
<h1 id="research">{{ research.heading | escape }}</h1>

{% for topic in research.topics %}
<section class="research-detail" aria-labelledby="{{ topic.id | escape }}">
  <h2 id="{{ topic.id | escape }}">{{ topic.title | escape }}</h2>
  {{ topic.body | markdownify }}
  {% if topic.image and topic.image != '' %}
  <figure class="research-figure">
    <img src="{{ topic.image | relative_url | escape }}" alt="{{ topic.image_alt | default: topic.title | escape }}" loading="lazy">
    {% if topic.caption and topic.caption != '' %}
    <figcaption>{{ topic.caption | markdownify | remove: '<p>' | remove: '</p>' | strip }}</figcaption>
    {% endif %}
  </figure>
  {% endif %}
  {% if topic.related_papers.size > 0 %}
  <ul class="research-papers">
    {% for paper in topic.related_papers %}
    <li><a href="{{ paper.url | relative_url | escape }}">{{ paper.label | escape }}</a></li>
    {% endfor %}
  </ul>
  {% endif %}
</section>
{% endfor %}

{% if research.education.size > 0 %}
<h2>{{ research.education_heading | escape }}</h2>
<ul>
  {% for entry in research.education %}
  <li>{{ entry | escape }}</li>
  {% endfor %}
</ul>
{% endif %}
