<h2 id="contact">Contact</h2>

{% if site.data.profile.email and site.data.profile.email != '' %}
<p>Email: <a href="mailto:{{ site.data.profile.email | escape }}">{{ site.data.profile.email | escape }}</a></p>
{% endif %}
{% if site.data.profile.affiliation and site.data.profile.affiliation != '' %}
<p>{% if site.data.profile.affiliation_link and site.data.profile.affiliation_link != '' %}<a href="{{ site.data.profile.affiliation_link | relative_url | escape }}">{{ site.data.profile.affiliation | escape }}</a>{% else %}{{ site.data.profile.affiliation | escape }}{% endif %}</p>
{% endif %}
