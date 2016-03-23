import os

from flask import Flask
from raven.contrib.flask import Sentry

app = Flask(__name__)
sentry = Sentry(app, dsn=os.environ['SENTRY_DSN'])

@app.route("/")
def hello():
	1/0

if __name__ == "__main__":
    app.run()