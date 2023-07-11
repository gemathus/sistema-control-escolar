from flask import Flask, render_template
from entities.estudiante import Estudiante
import os
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/estudiantes')
def estudiantes():
    students = []
    with open('db/estudiantes.txt', 'r') as f:
        lines = f.read().splitlines()
        for l in lines:
            data = l.split('|')
            students.append(Estudiante(data[0], data[1], data[2], data[3]))

    return render_template('estudiantes.html', data=students)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
