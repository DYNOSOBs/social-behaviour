# Add pictures to feed

## Branch branch branch

Firstly you need to branch (do not make changes to `master`).
To branch use the commands `git branch <name>` and `git checkout <name>`.

Name the branch as `new-images`. For example:

```shell
$ git branch new-images
$ git checkout new-images
```

## Add pictures

On our homepage, we have a feed of pictures. To add a picture to the feed, you
need to include that picture in the `original-images-feed folder`.

The pictures appear based on their name, so you should include the year and
month in the filename if you want it to appear as the latest on the feed.

Make sure the image is saved in `jpg` format.

The pictures are typically of high quality, which is great, but it
also means that every time someone loads the website, it can take time for all
the pictures to load, which we want to avoid. 

So, what do we do? We reduce the image quality. There are several tools for
that. One way to do it via the terminal, for all pictures at once, is to install
ImageMagick: [ImageMagick Download](https://imagemagick.org/script/download.php). 

Once you have installed the tool maybe you want to restart your terminal session.
Then, navigate to the website folder (directory) and the images folder `original-images-feed`
by running:

```shell
$ cd social-behaviour/original-images-feed/
```

The run the following command:

```shell
mogrify -path ../feed-imgs/ -monitor -quality 200 -trim -resize  '>'600x400 *.jpg
```


Once you have made all the necessary changes you can review them locally
by [compile the website](Installation.md).

When you are ready you need to `git add` the files you have changed/added,
then to `git commit` and finally `git push`. Your branch should appear
on GitHub. You can now go ahead and open a pull request.