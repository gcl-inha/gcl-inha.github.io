---
hide:
  - navigation
  - toc
---

# News

{% for item in news %}
- __{{ item.time }}__ {% if item.link %}<a href="{{ item.link }}" target="_blank">{{ item.title }}</a>{% else %}{{ item.title }}{% endif %}
{% endfor %}

<br />
