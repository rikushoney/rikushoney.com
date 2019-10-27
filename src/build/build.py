from jinja2 import Environment, FileSystemLoader


class JinjaBuild():
    def __init__(self, environment):
        self._environment = Environment(
            loader=FileSystemLoader(environment)
        )

    def stream_template(self, template, target):
        t = self._environment.get_template(template)
        t.stream().dump(target)

    def stream_templates(self, templates):
        for template in templates:
            self.stream_template(template["template"], template["target"])
