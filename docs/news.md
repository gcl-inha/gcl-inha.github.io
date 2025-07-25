---
hide:
  - navigation
  - toc
---

# News

{% for item in news %}
<div class="news-entry">
  <div class="news-time">{{ item.time }}</div>
  <div class="news-title">{{ item.title }}</div>
</div>
{% endfor %}