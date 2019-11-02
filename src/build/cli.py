import click

GLOBAL_CONTEXT_SETTINGS = {
    "help_option_names": ["-h", "--help"]
}


@click.group(context_settings=GLOBAL_CONTEXT_SETTINGS)
def main():
    pass


@main.command(context_settings=GLOBAL_CONTEXT_SETTINGS,
              help="Render the website")
@click.option("--base", "-b", default=".", show_default=True,
              help="The directory to load templates and static files from")
@click.option("--out", "-o", default="out", show_default=True,
              help="Output directory of website")
@click.option("--config", "-c", default="build.json", show_default=True,
              help="Config file to read build configuration from")
def website(out: str, base: str, config: str):
    try:
        import os

        out_path = os.path.abspath(out)
        base_path = os.path.abspath(base)
        config_file = os.path.abspath(config)

        if not os.path.exists(config_file):
            raise click.ClickException("No config file found")

        if not os.path.exists(out_path):
            os.mkdir(out_path)

        from .config_parser import ConfigParser
        cfg = ConfigParser(config)

        if not cfg.has("routes"):
            raise click.ClickException("No routes specified")

        from .pygments_build import PygmentsBuild

        pygments = PygmentsBuild()
        pygments.make_stylefile(os.path.join(out_path, "styles", "syntax.css"))

        from .jinja_build import JinjaBuild

        jinja = JinjaBuild(os.path.join(base_path, "templates"))
        jinja.render_templates(out_path, cfg["routes"])

        from .static_build import StaticBuild

        static = StaticBuild(os.path.join(base_path, "static"))
        static.copy_content(out_path)
    except Exception as error:
        raise error
        # raise click.ClickException(str(error))
