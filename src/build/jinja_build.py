from jinja2 import Environment, FileSystemLoader

import os


class JinjaBuild():
    def __init__(self, environment):
        self._environment = Environment(
            loader=FileSystemLoader(environment)
        )

    def render_template(self, template, target):
        """
        Renders the template using Jinja to a file ``target`` in the output directory
        if ``target`` is not an absolute path
        """
        t = self._environment.get_template(template)
        t.stream().dump(
            target if os.path.isabs(target) else os.path.join(self._out, target)
        )

    def render_templates(self, outpath, templates):
        """
        Renders a list of templates to their respective targets using :func:``render_template``
        The list must be in the format:

            [
                { "template": "example-template.html", "target": "example.html" },
                { "template": "example2-template.html", "target": "example2.html" }
            ]

        If ``target`` is omitted, ``template`` will be used as the output filename
        """
        for template in templates:
            self.render_template(
                template["template"],
                os.path.join(outpath, template["target"]) if "target" in template
                else os.path.join(outpath, template["template"])
            )
