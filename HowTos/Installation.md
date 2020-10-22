# Installation

In order to apply any changes to the website you must first `clone` the
repository to your machine and learn how to `compile` the website locally.

## Clone the repository

This is done by running the following command in your terminal:

```shell
$ git clone https://github.com/Nikoleta-v3/social-behaviour.git
```

## Compile the website locally

You can compile the website locally. The website requires Jekyll 3.0.

Run:

```shell
$ bundle install
```

if this is your first time installing it.

Once that the installation has completed you need to run the following commands
at the root of the directory:

```shell
$ bundle exec jekyll build

$ bundle exec jekyll serve
```

In the terminal/command prompt you can find the local address where the
website is currently hosted. It will look something like:

```shell
Server address: http://127.0.0.1:4000
```

Click on the address or copy paste the address in your browser (Safari for example).