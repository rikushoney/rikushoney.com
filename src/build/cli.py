from typing import Dict

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
def make(out: str, base: str, config: str):
    import json
    import os

    out_path = os.path.abspath(out)
    base_path = os.path.abspath(base)
    config_file = os.path.abspath(config)

    if not os.path.exists(config_file):
        raise click.ClickException("No config file found")

    if not os.path.exists(out_path):
        os.mkdir(out_path)

    cfg: Dict = {}
    with open(config_file, "r") as f:
        cfg = json.load(f)

    if "routes" not in cfg:
        raise click.ClickException("No routes specified")

    # Inject base path
    for template in cfg["routes"]:
        template["target"] = os.path.join(out_path, template["target"])

    from .build import JinjaBuild

    # TODO: inject static path into templates
    jinja = JinjaBuild(os.path.join(base_path, "templates"))
    jinja.stream_templates(cfg["routes"])

    from shutil import copytree, rmtree

    rmtree(os.path.join(out_path, "static"))

    copytree(
        os.path.join(base_path, "static"),
        os.path.join(out_path, "static"))
