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

<div id="alumni">
<h5>Alumni</h5>
<ul>
  <li> <b> Logan Cartau </b> (Intern). Coevolution of reciprocity and network topology. 2021</li>
</ul>
</div>
