from typing import Dict

if __name__ == "__main__":
    import json
    config: Dict = {}
    with open("build.json", "r") as config_file:
        config = json.load(config_file)

    stylefile = None

    import io
    import shutil

    from contextlib import redirect_stdout

    # Make pygments styles
    if "pygments" in config:
        from pygments import cmdline

        pygments_config = config["pygments"]
        style = "default"
        if "style" in pygments_config:
            style = pygments_config["style"]
        opts = [
            "pygmentize",
            "-f", "html",
            "-S", style,
            "-a", ".syntax"
        ]

        style_css = io.StringIO()
        with redirect_stdout(style_css):
            cmdline.main(opts)

        stylefile = "syntax.css"
        if "filename" in pygments_config:
            stylefile = pygments_config["filename"]
        with open(f"static/{stylefile}", "w") as syntax_file:
            style_css.seek(0)
            shutil.copyfileobj(style_css, syntax_file)

    # Render jinja pages
    from jinja2 import Environment, FileSystemLoader
    env = Environment(
        loader=FileSystemLoader("templates")
    )

    if "target" in config:
        import os
        os.mkdir(config["target"])

        for route in config["routes"]:
            template = env.get_template(route["name"])
            template.stream(
                pygments_filename=stylefile).dump(
                    f"{config['target']}/{route['name']}")
