#!/usr/bin/env python3

from livereload import Server, shell

server = Server()
server.watch('index.html')
server.watch('style.scss', shell('make style'))

server.serve(host='0.0.0.0', root='.')
