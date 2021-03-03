import subprocess
import webbrowser


def publications_updated():
    command = "git diff --name-only HEAD HEAD~1"
    file_to_check = "publications/index.md"

    result = subprocess.check_output(command, shell=True, text=True)

    return file_to_check in result


def get_publications_update():
    replace = {
        "+-": "",
        "+": "",
        "**": "",
        "_": "",
        "[": "",
        "]": "",
        "(": " ",
        ")": " ",
        "&": "",
        """<i class="fa fa-file-pdf-o"></i>""": "",
    }
    filename = "publications/index.md"
    command = f"git diff HEAD^ HEAD {filename}"
    output = subprocess.check_output(command, shell=True, text=True)

    raw_information = [
        line for line in output.split("\n")[:-1] if line[0] == "+"
    ][1:]
    information = "\n".join(raw_information)

    for expr in replace.items():
        information = information.replace(*expr)

    return information


def update_website():
    command = "scp -r _site/* glynatsi@web.evolbio.mpg.de:/srv/www/htdocs/social-behaviour/."
    subprocess.run(command, shell=True)


if __name__ == "__main__":  # pragma: no cover

    is_updated = publications_updated()

    if is_updated:
        information = get_publications_update()

        recipient = "martinsen@evolbio.mpg.de"
        subject = "Update on publications group of social behaviour"

        body = f"""
Hello Iben,

Our group recently published the following:

{information}

All the best,

Nikoleta
"""
        # email library
        webbrowser.open(
            "mailto:?to=" + recipient + "&subject=" + subject + "&body=" + body,
            new=1,
        )

    # # copy _site to server
    update_website()
