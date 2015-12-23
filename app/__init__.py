from flask import Flask, render_template

app = Flask(__name__)

from app.editor.controller import main_editor as editor

app.register_blueprint(editor)
