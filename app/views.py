"""
Process POST requests from clients, log data to files so it can be sent with filebeat
@author: degenerat3
"""

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
    arp = content['arp']

    log_fw(ip, fwall)
    #log_hosts(ip, hosts)
    #log_routes(ip, routes)
    #log_arp(ip, arp)

    return "Success"


@app.route('/scavpro', methods=['POST'])
def process_scavpro():
    content = request.json
    return "Success"