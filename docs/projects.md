---
hide:
  - navigation
  - toc
---

<style>
.md-typeset .grid {
    grid-template-columns: repeat(auto-fit, minmax(90%, 1fr))
}
</style>


# Project

## On-going

<div class="grid" markdown>

{% for item in projects.ongoing %}
<div class="card" markdown>
<div class="project-thumbnail-cell" markdown>
<img class="project-thumbnail" src="../assets/projects/{{ item.img }}" markdown>
</div>
<div class="project-description-cell" markdown>
__{{ item.ko }}__
<br>
{{ item.en }}
<br>
{{ item.date }}
<br>
{{ item.fund }}
</div>
</div>

{% endfor %}
</div>


<br />

