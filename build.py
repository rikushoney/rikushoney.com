#!/usr/bin/env python


from jinja2 import Environment, FileSystemLoader
import tomllib


def main():
    loader = FileSystemLoader(".")
    env = Environment(loader=loader)
    config = dict()
    with open("config.toml") as config_file:
        config.update(tomllib.loads(config_file.read()))
    index = env.get_template("index.html.jinja").render(**config)
    with open("index.html", "w") as index_file:
        index_file.write(index)


if __name__ == "__main__":
    main()
