<section class="home-news" aria-labelledby="news-heading">
  <div class="home-news-heading">
    <h2 id="news-heading">News</h2>
    <a href="{{ '/news/' | relative_url }}">All news</a>
  </div>
  {% include news-list.html limit=3 %}
</section>
