---
layout: archive
title:
modified:
tags: []
image:
  feature:
  teaser:
---

<h5>Current</h5>

<div class="tiles">
{% for post in site.categories.current reversed%}
  {% include people-grid.html %}
{% endfor %}
</div><!-- /.tiles -->

<div id="alumni">
<h5>Alumni</h5>
<ul>
  <li> <b> Vivien Kleinow </b> (MSc Student). October 2022 - November 2023</li>
  <li> <b> Moshe Hoffman </b> (Visiting Researcher). April 2021 - October 2022</li>
  <li> <b> Logan Cartau </b> (Intern). Coevolution of reciprocity and network topology. 2021</li>
</ul>
</div>
