#Импорт
from flask import Flask, render_template, request, redirect, url_for, flash



app = Flask(__name__)
app.secret_key = 'your_secret_key'

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form_result', methods=['POST'])
def form_result():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    print(f'Name: {name}, Email: {email}, Message: {message}')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)