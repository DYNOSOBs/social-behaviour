---
layout: archive
title: "People"
modified:
tags: []
image:
  feature:
  teaser:
---

<div class="tiles">
<h2 class="post-title">Current</h2>
{% for post in site.categories.current reversed%}
  {% include post-grid.html %}
{% endfor %}
</div><!-- /.tiles -->