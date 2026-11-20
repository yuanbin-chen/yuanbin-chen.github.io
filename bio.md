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
