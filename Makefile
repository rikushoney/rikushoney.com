SASS=sass

style.css: style.scss
	$(SASS)	$< $@

style: style.css

server: style
	pipenv run ./server.py

clean:
	rm style.css style.css.map

# vim: set noexpandtab tabstop=8 shiftwidth=8:
