alias b := build

build:
	python build.py

watch:
	watchexec -r -e js,css,html,toml,py -- python build.py

serve:
	livereload
