---
hide:
  - navigation
  - toc
---

# {{ config.site_name }}
인하대학교 생성컴퓨팅 연구실은 일반 사용자부터 분야별 전문가에 이르기까지, 누구나 생성형 AI의 혜택을 누릴 수 있도록 접근성과 사회적 효용을 극대화한 인간 중심의 기술을 연구합니다. 나아가 생성형 AI의 책임감 있는 발전을 위해 데이터 보안과 윤리적 가치를 보장하는 신뢰 시스템 구축에 주력하고 있습니다.

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
