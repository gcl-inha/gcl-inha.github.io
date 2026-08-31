---
hide:
  - navigation
  - toc
---

# Teaching

<div class="teaching-content" markdown>

{% for g in teaching.groups %}
**{{ g.title }}**

<ul class="teaching-courses">
{%- for c in g.courses %}
  <li>
    {%- if c.link -%}
      <a href="{{ c.link }}" target="_blank">{{ c.name }}</a>
    {%- else -%}
      {{ c.name }}
    {%- endif -%}
    {%- if c.note %} <span class="teaching-note">({{ c.note }})</span>{% endif %}
    <span class="teaching-term">{{ c.term }}</span>
  </li>
{%- endfor %}
</ul>
{% endfor %}

</div>

<br />
