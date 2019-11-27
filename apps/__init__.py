from flask import Flask, render_template
from apps.users import users_bp
import config

app = Flask(__name__)

app.register_blueprint(users_bp)

app.config.from_object(config)


@app.route('/')
def hello_world():
    # return 'Hello World!'
    return render_template('index.html')
