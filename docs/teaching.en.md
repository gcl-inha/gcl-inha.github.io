---
hide:
  - navigation
  - toc
---

# Teaching

<div class="teaching-content" markdown>

{% for sem in teaching.terms %}
**{{ sem.term }}**{% if sem.upcoming %} <em>(Upcoming)</em>{% endif %}

<ul class="teaching-courses">
{%- for c in sem.courses %}
  <li>
    {%- if c.link -%}
      <a href="{{ c.link }}" target="_blank">{{ c.name }}</a>
    {%- else -%}
      {{ c.name }}
    {%- endif -%}
    {%- if c.note %} ({{ c.note }}){% endif -%}
  </li>
{%- endfor %}
</ul>
{% endfor %}

</div>

<br />
