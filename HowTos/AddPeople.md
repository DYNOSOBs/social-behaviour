# Add People

In order to add your personal profile you must include a new file (`.md`) file
in `_posts/people/`.

Firstly you need to branch (do not make changes to `master`).
To branch use the commands `git branch <name>` and `git checkout <name>`.

Name the branch as `add-people-your_last_name`. For example:

```shell
$ git branch add-people-glynatsi
$ git checkout add-people-glynatsi
```

Once you have branched create a new `.md` file in `_posts/people/`. The name
of the file should follow the format `year-month-day-your_last_name.md` where:

- `year` is the year you joined the group
- `month` is the month you joined the group
- `day` is the day you joined the group (roughly)

For example:

```
_posts/people/2020-09-22-Glynatsi.md
```

The `year-month-day-your_last_name.md` should have the following format:

**Header**

The beginning of the file should include the following lines were you alter
the `title`, `excerpt` and `teaser` with your information.

```shell
---
layout: people
title: <your name>
excerpt: <your position>
categories: current
tags:
image:
  path: *image
  teaser: <your picture>
---
```

For the `teaser` you will need to give the name of your profile picture. Include
your picture in the `images` folder. 

For example in `images` folder there is a picture named `Glynatsi.jpg`, thus
`teaser: Glynatsi.jpg`.

An example of a **Header**:

```shell
---
layout: people
title: Dr Nikoleta E. Glynatsi
excerpt: Postdoc
categories: current
tags:
image:
  path: *image
  teaser: Glynatsi.jpg
---
```

**Main body**

The information you want to include.

The `.md` file stands for markdown. In this file you can use both markdown and
HTML syntax.

**Footer**

Include the following lines at the end of your file:


```html
<div id="socialMedia" style="text-align:center">
    <a href="<your_email>" title="Email"><i style="font-size:24px" class="fa fa-envelope"></i></a>
    <a href="<link_to_github_account>" title="GitHub"><i style="font-size:24px" class="fa fa-github"></i></a>
    <a href="<link_to_twitter>" title="Twitter"><i style="font-size:24px" class="fa fa-twitter"></i></a>
    <a href="<link_to_personal_profile>" title="Webpage"><i style="font-size:24px" class="fa fa-home"></i></a>
    <a href="<link_to_linked_in>" title="LinkedIn"><i style="font-size:24px" class="fa fa-linkedin"></i></a>
</div>

<img src="../../images/<your_picture>" class="center">
```

You need to alter:

- <your_email>
- <link_to_github_account>
- <link_to_twitter>
- <link_to_personal_profile>
- <link_to_linked_in>
- <your_picture>

If you are not using all of the following social apps just remove the equivalent
line.

```html
<div id="socialMedia" style="text-align:center">
    <a href="<your_email>" title="Email"><i style="font-size:24px" class="fa fa-envelope"></i></a>
    <a href="<link_to_github_account>" title="GitHub"><i style="font-size:24px" class="fa fa-github"></i></a>
    <a href="<link_to_twitter>" title="Twitter"><i style="font-size:24px" class="fa fa-twitter"></i></a>
    <a href="<link_to_personal_profile>" title="Webpage"><i style="font-size:24px" class="fa fa-home"></i></a>
    <a href="<link_to_linked_in>" title="LinkedIn"><i style="font-size:24px" class="fa fa-linkedin"></i></a>
</div>

<img src="../../images/<your_picture>" class="center">
```


Once you have added your personal `md` file check the locally hosted website to
view the changes.