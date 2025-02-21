#!/usr/bin/env python

import sys
import yaml
from jinja2 import Environment, FileSystemLoader
from os import listdir

env = Environment(
    loader=FileSystemLoader('./'),
)

template = env.get_template('site.html.j2')
if len(sys.argv) > 1:
    site_yaml = sys.argv[1]
else:
    site_yaml = "site.yaml"

cssFiles = []
for css in listdir("./styles"):
    cssFiles.append("./styles/" + css)

with open(site_yaml, 'r') as file:
    site = yaml.load(file, Loader=yaml.FullLoader)

    name = site["name"]
    title = site["title"]
    info = site["info"]
    intro = site["intro"]
    projects = site["projects"]

    html = template.render(name = name,
                           title = title,
                           info = info,
                           intro = intro,
                           projects = projects,
                           cssFiles = cssFiles)

    options = {
      "enable-local-file-access": None,
      "page-size": "Letter",
      "margin-top": "2",
      "margin-right": "2",
      "margin-bottom": "2",
      "margin-left": "2",
      "encoding": "UTF-8"
    }

    with open('index.html', 'w') as f:
        f.write(html)

    # pdfkit.from_string(html, "site.pdf", options=options, css=cssFiles)