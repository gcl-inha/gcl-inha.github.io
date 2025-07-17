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


# Publications


{% for year in publications.years %}
## {{ year.year }}

<div class="grid" markdown>

{% for paper in year.papers %}

<div class="card" markdown>
<div class="publication-thumbnail-cell" markdown>
<img class="publication-thumbnail" src="../assets/papers/{{ paper.img }}" markdown>
</div>
<div class="publication-description-cell" markdown>
{% if paper.project %}
<a class="fg-color-dark" href="{{ paper.project }}" target=_blank>__{{ paper.title }}__</a>
{% elif paper.arXiv %}
<a class="fg-color-dark" href="{{ paper.arXiv }}" target=_blank>__{{ paper.title }}__</a>
{% elif paper.link %}
<a class="fg-color-dark" href="{{ paper.link }}" target=_blank>__{{ paper.title }}__</a>
{% else %}
__{{ paper.title }}__
{% endif %}<br>
{% for author in paper.authors %}{% if author.name == people.professor.name %}<a href="{{ people.professor.web }}" target=_blank>{{ author.name }}</a>{% elif author.name == people.professor.legacy_name %}<a href="{{ people.professor.web }}" target=_blank>{{ author.name }}</a>{% elif author.link %}<a href="{{ author.link }}" target=_blank>{{ author.name }}</a>{% else %}{{ author.name }}{% endif %}{{ ", " if not loop.last else "" }}{% endfor %}{% if paper.authors_note %} (\* {{ paper.authors_note }}){% endif %}<br>
{{ paper.venue }} {% if paper.publication_note %}__({{ paper.publication_note }})__{% endif %}<br>
{% if paper.project %}<a href="{{ paper.project }}" target=_blank>Project</a>&ensp;&ensp;{% endif %}{% if paper.link %}<a href="{{ paper.link }}" target=_blank>LINK</a>&ensp;&ensp;{% endif %}{% if paper.arXiv %}<a href="{{ paper.arXiv }}" target=_blank>ARXIV</a>&ensp;&ensp;{% endif %}{% if paper.pdf %}<a href="{{ paper.pdf }}" target=_blank>Link</a>&ensp;&ensp;{% endif %}{% if paper.slides %}<a href="{{ paper.slides }}" target=_blank>Slides</a>&ensp;&ensp;{% endif %}{% if paper.poster %}<a href="{{ paper.poster }}" target=_blank>Poster</a>&ensp;&ensp;{% endif %}{% if paper.video %}<a href="{{ paper.video }}" target=_blank>Video</a>&ensp;&ensp;{% endif %}{% if paper.web_demo %}<a href="{{ paper.web_demo }}" target=_blank>Web Demo</a>&ensp;{% endif %}{% if paper.supplementary %}<a href="{{ paper.supplementary }}" target=_blank>Supplementary</a>&ensp;&ensp;{% endif %}{% if paper.code %}<a href="{{ paper.code }}" target=_blank>Code</a>&ensp;&ensp;{% endif %}{% if paper.hugging_face %}<a href="{{ paper.hugging_face }}" target=_blank>Hugging Face</a>&ensp;{% endif %}{% if paper.press_release %}{% for press_release in paper.press_release %}<a href="{{ press_release.link }}" target=_blank>Media {{ loop.index }}</a>&ensp;&ensp;{% endfor %}{% endif %}
</div>
</div>

{% endfor %}

</div>

{% endfor %}

<br />

