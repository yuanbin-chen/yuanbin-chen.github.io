---
layout: default
title: Bio
editorial: bio
permalink: /bio/
full_width: true
---

{% assign bio = site.data.bio %}
<h1 class="page-title">{{ bio.heading | escape }}</h1>

<div class="biography-copy">
  {{ bio.body | markdownify }}
</div>

{% if bio.education.size > 0 %}
<h2 id="education">{{ bio.education_heading | escape }}</h2>
<ul>
  {% for entry in bio.education %}
  <li>{{ entry | escape }}</li>
  {% endfor %}
</ul>
{% endif %}
