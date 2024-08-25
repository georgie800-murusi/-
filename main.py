#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы

@app.route('/form_result')
def form_result():
    button_energy = request.form.get('button_energy')
    return render_template('form_result.html')


if __name__ == "__main__":
    app.run(debug=True)