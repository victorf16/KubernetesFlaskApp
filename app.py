from flask import Flask, render_template
import socket
import sys
import re

app = Flask(__name__)

# Get the Docker host name
docker_host = socket.gethostname()

# Get the Python version
python_version = re.search(r'\d+\.\d+\.\d+', sys.version).group()

@app.route('/')
def index():
    return render_template('signup.html', host=docker_host, python_version=python_version)


@app.route('/verificapod')
def verificapod():
    return render_template('verificapod.html', host=docker_host, python_version=python_version)

@app.route('/fidel')
def fidel():
    return render_template('fidel.html', host=docker_host, python_version=python_version)


if __name__ == '__main__':
    app.run()
