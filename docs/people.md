---
hide:
  - navigation
  - toc
---

# People

## Professor

<div class="grid" markdown>

{% set item = people.professor %}
<div class="card" markdown>
<!-- <div class="people-thumbnail-cell" markdown>
<img class="people-thumbnail" src="../assets/profile/{{ item.name }}.png" markdown>
</div> -->
<div class="people-description-cell" markdown>
{% if item.web %}<a class="fg-color-dark" href="{{ item.web }}" target="_blank">__{{ item.name }}__</a>{% else %}__{{ item.name }}__{% endif %}<br>
{{ item.type }}<br>
{% if item.web %}<a class="fg-color-dark"href="{{ item.web }}" target="_blank">:fontawesome-solid-house:</a>&nbsp; {% endif %}{% if item.email %}<a class="fg-color-dark" href="mailto:{{ item.email }}" target="_top">:fontawesome-solid-envelope:</a>&nbsp; {% endif %}{% if item.twitter %} <a class="fg-color-dark" href="{{ item.twitter }}" target="_blank">:fontawesome-brands-x-twitter:</a>&nbsp; {% endif %}{% if item.linkedin %} <a class="fg-color-dark" href="{{ item.linkedin }}" target="_blank">:fontawesome-brands-linkedin:</a>&nbsp; {% endif %}{% if item.github %} <a class="fg-color-dark" href="{{ item.github }}" target="_blank">:fontawesome-brands-github:</a>&nbsp; {% endif %}{% if item.scholar %}<a class="fg-color-dark"class="fg-color-dark" href="{{ item.scholar }}" target="_blank">:fontawesome-brands-google-scholar:</a>&nbsp;{% endif %}{% if item.cv %} <a class="fg-color-dark" href="{{ item.cv }}" target="_blank">:fontawesome-solid-file:</a>&nbsp; {% endif %}
</div>
</div>

</div>
<br>


<!-- ## Ph.D. Students

<div class="grid" markdown>

{% for item in people.phd %}
<div class="card" markdown>
<div class="people-thumbnail-cell" markdown>
<img class="people-thumbnail" src="../assets/profile/{{ item.name }}.png" markdown>
</div>
<div class="people-description-cell" markdown>
{% if item.web %}<a href="{{ item.web }}" target="_blank">__{{ item.name }}__</a>{% else %}__{{ item.name }}__{% endif %}<br>
{{ item.type }}<br>
{% if item.web %}<a href="{{ item.web }}" target="_blank">:fontawesome-solid-house:</a>&nbsp; {% endif %}{% if item.email %}<a href="mailto:{{ item.email }}" target="_top">:fontawesome-solid-envelope:</a>&nbsp; {% endif %}{% if item.twitter %} <a href="{{ item.twitter }}" target="_blank">:fontawesome-brands-x-twitter:</a>&nbsp; {% endif %}{% if item.linkedin %} <a href="{{ item.linkedin }}" target="_blank">:fontawesome-brands-linkedin:</a>&nbsp; {% endif %}{% if item.github %} <a href="{{ item.github }}" target="_blank">:fontawesome-brands-github:</a>&nbsp; {% endif %}{% if item.cv %} <a href="{{ item.cv }}" target="_blank">:academicons-cv:</a>&nbsp; {% endif %}
</div>
</div>
{% endfor %}

</div> 
<br>
-->


## Master's Students

<div class="grid" markdown>

{% for item in people.master %}
<div class="card" markdown>
<!-- <div class="people-thumbnail-cell" markdown>
<img class="people-thumbnail" src="../assets/profile/{{ item.name }}.png" markdown>
</div> -->
<div class="people-description-cell" markdown>
{% if item.web %}<a class="fg-color-dark" href="{{ item.web }}" target="_blank">__{{ item.name }}__</a>{% else %}__{{ item.name }}__{% endif %}<br>
{{ item.type }}<br>
{% if item.web %}<a class="fg-color-dark"href="{{ item.web }}" target="_blank">:fontawesome-solid-house:</a>&nbsp; {% endif %}{% if item.email %}<a class="fg-color-dark" href="mailto:{{ item.email }}" target="_top">:fontawesome-solid-envelope:</a>&nbsp; {% endif %}{% if item.twitter %} <a class="fg-color-dark" href="{{ item.twitter }}" target="_blank">:fontawesome-brands-x-twitter:</a>&nbsp; {% endif %}{% if item.linkedin %} <a class="fg-color-dark" href="{{ item.linkedin }}" target="_blank">:fontawesome-brands-linkedin:</a>&nbsp; {% endif %}{% if item.github %} <a class="fg-color-dark" href="{{ item.github }}" target="_blank">:fontawesome-brands-github:</a>&nbsp; {% endif %}{% if item.scholar %}<a class="fg-color-dark"class="fg-color-dark" href="{{ item.scholar }}" target="_blank">:fontawesome-brands-google-scholar:</a>&nbsp;{% endif %}{% if item.cv %} <a class="fg-color-dark" href="{{ item.cv }}" target="_blank">:fontawesome-solid-file:</a>&nbsp; {% endif %}
</div>
</div>
{% endfor %}

</div>
<br>


## Undergraduate Students

<div class="grid" markdown>
{% for item in people.undergrads %}
<div class="card" markdown>
{% if item.email %}
<!-- <div class="people-thumbnail-cell" markdown>
<img class="people-thumbnail" src="../assets/profile/{{ item.name }}.png" markdown>
</div> -->
<div class="people-description-cell" markdown>
{% if item.web %}<a href="{{ item.web }}" target="_blank">__{{ item.name }}__</a>{% else %}__{{ item.name }}__{% endif %}<br>
{{ item.type }}<br>
{% if item.web %}<a class="fg-color-dark"href="{{ item.web }}" target="_blank">:fontawesome-solid-house:</a>&nbsp; {% endif %}{% if item.email %}<a class="fg-color-dark" href="mailto:{{ item.email }}" target="_top">:fontawesome-solid-envelope:</a>&nbsp; {% endif %}{% if item.twitter %} <a class="fg-color-dark" href="{{ item.twitter }}" target="_blank">:fontawesome-brands-x-twitter:</a>&nbsp; {% endif %}{% if item.linkedin %} <a class="fg-color-dark" href="{{ item.linkedin }}" target="_blank">:fontawesome-brands-linkedin:</a>&nbsp; {% endif %}{% if item.github %} <a class="fg-color-dark" href="{{ item.github }}" target="_blank">:fontawesome-brands-github:</a>&nbsp; {% endif %}{% if item.scholar %}<a class="fg-color-dark"class="fg-color-dark" href="{{ item.scholar }}" target="_blank">:fontawesome-brands-google-scholar:</a>&nbsp;{% endif %}{% if item.cv %} <a class="fg-color-dark" href="{{ item.cv }}" target="_blank">:fontawesome-solid-file:</a>&nbsp; {% endif %}
</div>
{% else %}
<div class="people-thumbnail-cell" markdown>
</div>
<div class="people-description-cell" markdown>
__{{ item.name }}__
</div>
{% endif %}
</div>
{% endfor %}
</div>
<br>

<!-- ## Former Graduate Students

<div class="grid" markdown>

{% for item in people.former_graduates %}
<div class="card" markdown>
<div class="people-thumbnail-cell" markdown>
<img class="people-thumbnail" src="../assets/profile/{{ item.name }}.png" markdown>
</div>
<div class="people-description-cell" markdown>
{% if item.web %}<a href="{{ item.web }}" target="_blank">__{{ item.name }}__</a>{% else %}__{{ item.name }}__{% endif %}<br>
{{ item.type }}<br>
{% if item.now %} Now at {{ item.now }} {% endif %}
</div>
</div>
{% endfor %}

</div> -->


## Former Undergraduate Students

<div class="grid" markdown>
{% for item in people.former_undergrads %}
<div class="card" markdown>
__{{ item.name }}__
</div>
{% endfor %}
</div>
