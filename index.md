---
layout: home
permalink: /
image:
  feature: home.jpg
---

<h5>Welcome</h5>

We are a research group at the Max Planck Institute for Evolutionary Biology.

Our group explores under which conditions individuals cooperate. To this end, we
translate social interactions into strategic games. These games can then be
explored mathematically, with computer simulations, and with behavioral
experiments.

<h5>Feed</h5>

<!-- {% assign filenames = "new-group-img.jpg,summer-trip.jpeg,xmas-brunch.jpg,xmas-walk.jpg" | split: "," %}
<div class ="image-gallery">
{% for name in filenames %}
    <div class="box">
    <a href="{{ site.imagesurl }}{{ name }}">
      <img src="{{ site.thumbsurl }}{{ name }} " alt="{{ name }}"  class="img-gallery" />
     </a>
    </div>
 {% endfor %}
</div> -->

{% include image-gallery.html folder="feed" %}