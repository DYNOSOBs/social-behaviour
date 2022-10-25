---
layout: archive
title:
modified:
tags: []
image:
  feature:
  teaser:
---

<div class="tiles">
<h5 class="post-title">Current</h5>
{% for post in site.categories.current reversed%}
  {% include people-grib.html %}
{% endfor %}
</div><!-- /.tiles -->

<div id="alumini">
<h5>Alumini</h5>
<ul>
  <li> <b> Moshe Hoffman </b> (Visiting Researcher). April 2021 - October 2022</li>
  <li> <b> Logan Cartau </b> (Intern). Coevolution of reciprocity and network topology. 2021</li>
</ul>
</div>
