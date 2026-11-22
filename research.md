---
layout: default
title: Research
editorial: research
permalink: /research/
full_width: true
---

{% assign research = site.data.research %}
<h1 id="research" class="page-title">{{ research.heading | escape }}</h1>

{% assign research_topics = site.research_topics | sort: 'order', 'last' %}
{% for topic in research_topics %}
{% assign topic_id = topic.relative_path | split: '/' | last | remove: '.md' %}
<section class="research-detail" aria-labelledby="{{ topic_id | escape }}">
  <h2 id="{{ topic_id | escape }}">{{ topic.title | escape }}</h2>
  {{ topic.overview | markdownify }}
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
    {% for paper_path in topic.related_papers %}
    {% assign paper = site.papers | where: 'relative_path', paper_path | first %}
    {% if paper %}
    {% assign paper_id = paper_path | split: '/' | last | remove: '.md' %}
    <li><a href="{{ '/publications/#' | append: paper_id | relative_url | escape }}">{{ paper.title | escape }}</a></li>
    {% endif %}
    {% endfor %}
  </ul>
  {% endif %}
</section>
{% endfor %}
