from flask import render_template
from src import app


@app.route('/contacto')
def contacto():
    return 'En contacto'