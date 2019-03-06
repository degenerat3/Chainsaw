"""
Process POST requests from clients, log data to files so it can be sent with filebeat
@author: degenerat3, knif3
"""

from app import app

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
