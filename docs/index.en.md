---
hide:
  - navigation
  - toc
---

# {{ config.site_name }}
At the Generative Computing Lab (GCL), we build human-centric solutions to make Generative AI more accessible and impactful for both the public and expert professionals. Above all, we prioritize the responsible use of Generative AI, developing robust frameworks to safeguard data security and ensure ethical deployment.

<!-- Link Swiper's CSS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />

<!-- Research Highlights -->
<div class="swiper research-highlights-swiper" markdown>

## Research Highlights
<div class="swiper-wrapper" markdown>

{% for paper in research_highlights %}
<div class="swiper-slide" markdown>

<a href="{{ paper.link }}" target=_blank>
<div class="card" markdown>
<center>
<img src="/assets/highlights/{{ paper.key }}.png" markdown>
<b>{{ paper.title }} ({{ paper.venue }})</b><br>
<span class="fg-color-dark">{{ paper.desc }}</span><br>
</center>
</div>
</a>

</div>
{% endfor %}

</div>
<div class="swiper-pagination"></div>
</div>


<div class="container" markdown>
<!-- News -->
<div class="news" markdown>
<h2><a class="fg-color-dark" href="news/">News</a></h2>
{% for item in news %}
{% if loop.index <= 5 %}
<div class="news-entry">
  <div class="news-time">{{ item.time }}</div>
  <div class="news-title">{{ item.title }}</div>
</div>
{% endif %}
{% endfor %}
</div>
</div>

<br><br>


<!-- Swiper JS -->
<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>

<!-- Initialize Swiper -->
<script>
var swiper = new Swiper(".research-highlights-swiper", {
    spaceBetween: 30,
    centeredSlides: true,
    autoplay: {
        delay: 5000,
        disableOnInteraction: false,
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
});
</script>