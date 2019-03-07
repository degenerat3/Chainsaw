import datetime
import os
from flask import Flask, request
from . import app
from .log import *

@app.route('/campfire', methods=['POST'])
def process_campfire():
    content = request.json
    ip = content['ip']
    fwall = content['rules']
    hosts = content['etchosts']
    routes = content['routes']

    log_fw(ip, fwall)
    log_hosts(ip, hosts)
    log_routes(ip, routes)

    return "Success"


@app.route('/scavpro', methods=['POST'])
def process_scavpro():
    content = request.json
    ip = content['IP']
    creds = content['credentials']
    log_creds(ip, creds)
    return "Success"