---
layout: default
title: Honors
editorial: honors
permalink: /honors/
full_width: true
activities: true
---

{% assign honors = site.data.honors %}
<h1 id="honors-and-awards" class="page-title">{{ honors.heading | escape }}</h1>

<dl class="academic-timeline">
  {% for honor in honors.items %}
  <dt>{{ honor.date | escape }}</dt><dd>{{ honor.title | escape }}</dd>
  {% endfor %}
</dl>
