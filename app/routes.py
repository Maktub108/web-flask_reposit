from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    user_data = None
    if request.method == 'POST':
        # Получение данных из формы
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')
        # Проверка и подготовка данных для отображения
        if name and city and hobby and age:
            user_data = {
                'name': name,
                'city': city,
                'hobby': hobby,
                'age': age
            }
        else:
            # Можно добавить обработку ошибок или уведомлений
            pass
    return render_template('index.html', user_data=user_data)

if __name__ == '__main__':
    app.run(debug=True)