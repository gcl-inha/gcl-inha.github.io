---
hide:
  - navigation
  - toc
---

<style>
.md-typeset .grid {
  grid-template-columns: repeat(auto-fit, minmax(90%, 1fr));
}

/* 연구실 구성원(교수+학생 전원) 밑줄: dashed + descender 겹침 방지 */
.md-content .md-typeset a.lab-member,
.md-content .md-typeset .lab-member {
  text-decoration: none !important;
  border-bottom: 1.5px dashed var(--md-primary-fg-color);
}
.md-content .md-typeset a.lab-member:hover,
.md-content .md-typeset .lab-member:hover {
  border-bottom-style: solid;
}
</style>

# Publications

{% set ns = namespace(lab_members=[]) %}

{%- if people.professor and people.professor.name -%}
  {%- set ns.lab_members = ns.lab_members + [ (people.professor.name.split('(')[0] | trim) ] -%}
{%- endif -%}

{%- for group in [people.phd, people.master, people.undergrads, people.former_graduates, people.former_undergrads] if group -%}
  {%- for p in group if p.name -%}
    {%- set ns.lab_members = ns.lab_members + [ (p.name.split('(')[0] | trim) ] -%}
  {%- endfor -%}
{%- endfor -%}

{%- for year in publications.years -%}
<h2>{{ year.year }}</h2>
<div class="grid">

{%- for paper in year.papers -%}
<div class="card">

  <div class="publication-thumbnail-cell">
    <img class="publication-thumbnail" src="../assets/papers/{{ paper.img }}">
  </div>

  <div class="publication-description-cell">
    {# ----- Title ----- #}
    <span class="pub-title"><strong>{{ paper.title }}</strong></span><br>

    {# ----- Authors ----- #}
    {%- for author in paper.authors -%}
      {%- set author_display = author.name -%}
      {%- set author_key = (author.name | replace('*','') | trim) -%}

      {%- if author_key in ns.lab_members -%}
        {%- if author.link -%}
          <a class="lab-member" href="{{ author.link }}" target="_blank">{{ author_display }}</a>
        {%- else -%}
          <span class="lab-member">{{ author_display }}</span>
        {%- endif -%}
      {%- else -%}
        {%- if author.link -%}
          <a href="{{ author.link }}" target="_blank">{{ author_display }}</a>
        {%- else -%}
          {{ author_display }}
        {%- endif -%}
      {%- endif -%}
      {%- if not loop.last -%}, {% endif -%}
    {%- endfor -%}
    {%- if paper.authors_note -%} (* {{ paper.authors_note }}){%- endif -%}
    <br>

    {{ paper.venue }}{%- if paper.publication_note -%} <strong>({{ paper.publication_note }})</strong>{%- endif -%}<br>

    {%- if paper.project %}<a href="{{ paper.project }}" target="_blank">Project</a>&ensp;&ensp;{%- endif -%}
    {%- if paper.link %}<a href="{{ paper.link }}" target="_blank">LINK</a>&ensp;&ensp;{%- endif -%}
    {%- if paper.arXiv %}<a href="{{ paper.arXiv }}" target="_blank">ARXIV</a>&ensp;&ensp;{%- endif -%}
    {%- if paper.pdf %}<a href="{{ paper.pdf }}" target="_blank">Link</a>&ensp;&ensp;{%- endif -%}
    {%- if paper.slides %}<a href="{{ paper.slides }}" target="_blank">Slides</a>&ensp;&ensp;{%- endif -%}
    {%- if paper.poster %}<a href="{{ paper.poster }}" target="_blank">Poster</a>&ensp;&ensp;{%- endif -%}
    {%- if paper.video %}<a href="{{ paper.video }}" target="_blank">Video</a>&ensp;&ensp;{%- endif -%}
    {%- if paper.web_demo %}<a href="{{ paper.web_demo }}" target="_blank">Web Demo</a>&ensp;{%- endif -%}
    {%- if paper.supplementary %}<a href="{{ paper.supplementary }}" target="_blank">Supplementary</a>&ensp;&ensp;{%- endif -%}
    {%- if paper.code %}<a href="{{ paper.code }}" target="_blank">Code</a>&ensp;&ensp;{%- endif -%}
    {%- if paper.hugging_face %}<a href="{{ paper.hugging_face }}" target="_blank">Hugging Face</a>&ensp;{%- endif -%}
    {%- if paper.press_release -%}
      {%- for pr in paper.press_release -%}
        <a href="{{ pr.link }}" target="_blank">Media {{ loop.index }}</a>&ensp;&ensp;
      {%- endfor -%}
    {%- endif -%}
  </div> <!-- /.publication-description-cell -->

</div> <!-- /.card -->
{%- endfor -%}

</div> <!-- /.grid -->
{%- endfor -%}

<br />