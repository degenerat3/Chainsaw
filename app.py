"""
Process POST requests from clients, log data to files so it can be sent with filebeat
@author: degenerat3, knif3
"""

import os
from app import app

if __name__ == '__main__':
    host = os.environ.get("FLASK_HOST", "0.0.0.0")
    port = os.environ.get("FLASK_PORT", "5000")
    debug = os.environ.get("FLASK_DEBUG", "True")
    debug = debug.lower().strip() in ["true", "yes", "1", "t"]
    app.run(debug=debug, host=host, port=port)
