# Add Publication

In order to add your new publication you need to edit the file `publications/index.md`.

Firstly you need to branch (do not make changes to `master`).
To branch use the commands `git branch <name>` and `git checkout <name>`.

Name the branch as `short-publication-title`. For example:

```shell
$ git branch future-egt
$ git checkout future-egt
```

**Uploading Paper**

Once you are on your new branch add a copy of your paper in the folder
`publications/papers`. There is no convention regarding naming the `pdf` file,
however, try to use sensible names and avoid abstract names such as `main.pdf`
or `mypaper.pdf`. Also avoid spaces and use `_` instead.

Once you have copied your paper in the folder you are ready to edit
the `publications/index.md`.

**Listing your Paper on the Website**

Edit the top the file `publications/index.md`. Each entry starts with the
symbol `-`, for example:

```shell
- Juan Li, Xiaowei Zhao, Bing Li, Charlotte S. L. Rossetti, Christian Hilbe, Haoxiang Xia
[**Evolution of cooperation through cumulative reciprocity**](https://www.nature.com/articles/s43588-022-00334-w)
_Nature Computational Science_ (2022) <a href="papers/CURE_ncs_2022.pdf"><i class="fa fa-file-pdf-o"></i>
```

The convention is the following:

```shell
- Author Name, Normal Text [**Title in bold**](link to paper) _Journal Name_ (year)
<a href="papers/<your paper>.pdf"><i class="fa fa-file-pdf-o"></i>
```

Once you have made all the necessary changes you can review them locally
by [compile the website](Installation.md).

When you are ready you need to `git add` the files you have changed/added,
then to `git commit` and finally `git push`. Your branch should appear
on GitHub. You can now go ahead and open a pull request.