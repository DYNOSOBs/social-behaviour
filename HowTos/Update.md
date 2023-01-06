# Update website

Once new changes have been merged into the `master` branch we need to update the
website.

The repository contains a script called `update.py`. Run the script with the following
command:

```shell
$ python update.py
```

The update script initially compiles the website. This creates a static version
of the website in the folder `_site`. This folder needs to be copied to the Max
Planck server. The script does that for you. Keep an eye on the terminal, you
need to enter a password.