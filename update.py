import subprocess
import webbrowser


def compile_website():
    command = "bundle exec jekyll build"
    subprocess.run(command, shell=True)


def update_website():
    command = "scp -r _site/* glynatsi@web.evolbio.mpg.de:/srv/www/htdocs/social-behaviour/."
    subprocess.run(command, shell=True)


if __name__ == "__main__":  # pragma: no cover

    # compile website
    compile_website()

    # copy _site to server
    update_website()
