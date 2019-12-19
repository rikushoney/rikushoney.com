from setuptools import setup, find_packages


setup(
    name="rikushoney-website",
    version="0.1-dev1",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "click",
        "markdown",
        "pygments",
        "jinja2",
        "livereload"
    ],
    entry_points={
        "console_scripts": [
            "website = build.cli:main"
        ]
    }
)
