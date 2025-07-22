---
hide:
  - navigation
  - toc
---

# {{ config.site_name }}
The Generative Computing Lab (GCL) at Inha University advances Generative AI (Gen AI) technologies to ensure that a wide range of people can benefit from them. We focuse on (but is not limited to) diffusion models and their applications, Gen AI + X (Gen AI for various domains) and ethical and responsible use of Gen AI.
<div class="ko">
인하대학교 생성컴퓨팅 연구실은 다양한 사람들이 혜택을 누릴 수 있는 생성형 AI 기술 개발을 목표로 연구를 수행하고 있습니다. 주요 연구 분야는 확산 모델(Diffusion Models)의 응용, 생성형 AI의 다양한 도메인 적용(Gen AI + X), 그리고 생성형 AI의 윤리적이고 책임 있는 활용 방안 등이 있습니다.
</div>

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
<img src="assets/highlights/{{ paper.key }}.png" markdown>
<b>{{ paper.title }} ({{ paper.venue }})</b><br>
<span class="fg-color-dark">{{ paper.desc }}</span><br>
<span class="fg-color-dark">{{ paper.desc_ko }}</span><br>
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
<h2><a class="fg-color-dark" href="/news">News</a></h2>
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