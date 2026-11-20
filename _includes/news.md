{% assign home = site.data.home %}
<section class="home-news" aria-labelledby="news-heading">
  <div class="home-news-heading">
    <h2 id="news-heading">{{ home.news_heading | escape }}</h2>
    <a href="{{ '/news/' | relative_url }}">{{ home.news_link_label | escape }}</a>
  </div>
  {% include news-list.html limit=home.news_count %}
</section>
