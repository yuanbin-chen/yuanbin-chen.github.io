{% for link in site.data.navigation.main %}
  {% assign nav_url = link.url | relative_url %}
  <a class="normal{% if link.right %} right{% endif %}" href="{{ nav_url | escape }}"{% if nav_url == page.url or link.url == page.url %} aria-current="page"{% endif %}>{{ link.title | escape }}</a>
{% endfor %}
