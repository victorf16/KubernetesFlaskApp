from flask import Flask, render_template
import socket

app = Flask(__name__)

# Get the Docker host name
docker_host = socket.gethostname()


@app.route('/')
def index():
    return render_template('index.html', host=docker_host)


@app.route('/signup')
def signup():
    return render_template('signup.html', host=docker_host)


if __name__ == '__main__':
    app.run()
