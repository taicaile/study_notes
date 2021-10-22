import codecs
import os
import re


rootPath = "https://nbviewer.jupyter.org/github/taicaile/study_notes/tree/master/"

dirs = sorted(os.listdir())
r = re.compile("[0-9]{3}_")
links = [rootPath + _dir for _dir in dirs if r.match(_dir)]

with codecs.open("README.md", "w+", encoding="utf8") as f:
    f.write("# Study Notes\n")
    for _link in links:
        f.write(
            " - [{}]({})".format(os.path.basename(_link), _link.replace(" ", "%20"))
        )
        f.write("\n")
