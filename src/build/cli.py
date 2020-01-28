import click
import functools
import os

from .build import build_website
from .live_server import start_live_server

GLOBAL_CONTEXT_SETTINGS = {
    "help_option_names": ["-h", "--help"]
}


def common_params(func):
    @click.option("--base", "-b", default=".", show_default=True,
                  help="The directory to load templates and static files from")
    @click.option("--out", "-o", default="out", show_default=True,
                  help="Output directory of website")
    @click.option("--config", "-c", default="build.yaml", show_default=True,
                  help="Config file to read build configuration from")
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@click.group(context_settings=GLOBAL_CONTEXT_SETTINGS)
def main():
    pass


def sanetize_args(out, base, config):
    return os.path.abspath(out), os.path.abspath(base), os.path.abspath(config)


@main.command(context_settings=GLOBAL_CONTEXT_SETTINGS,
              help="Render the website")
@common_params
def build(out, base, config):
    build_website(*sanetize_args(out, base, config))


@main.command(context_settings=GLOBAL_CONTEXT_SETTINGS,
              help="Start a live debug server")
@common_params
@click.option("--port", "-p", default=5500, show_default=True,
              help="Port to bind the server to")
def live(port: str, out: str, base: str, config: str):
    start_live_server(port, *sanetize_args(out, base, config))
