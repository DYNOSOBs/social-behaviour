---
layout: archive
title: "People"
modified:
tags: []
image:
  feature:
  teaser:
---

**Current**
<div class="tiles">
{% for post in site.categories.current reversed%}
  {% include post-grid.html %}
{% endfor %}
</div><!-- /.tiles -->

<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>

**Past**
<div class="tiles">
{% for post in site.categories.past reversed%}
  {% include post-grid.html %}
{% endfor %}
</div><!-- /.tiles -->