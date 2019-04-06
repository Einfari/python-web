import time
import json
import os
from aiohttp import web
from datetime import datetime
import asyncio
import logging
logging.basicConfig(level=logging.INFO)


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>')


def init():
    app = web.Application()
    app.router.add_route('GET', '/', index)
    web.run_app(app, host='127.0.0.1', port='8080')
    logging.info('Server started at http://127.0.0.1:8080...')
    return srv


init()
