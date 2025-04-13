from flask import Flask, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# Конфигурация базы данных
DATABASE = 'raspisanie2.db'  # Укажите имя вашего SQLite файла базы данных

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Позволяет обращаться к столбцам по имени
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rasp')
def schedule():
    # Подключение к базе данных
    conn = get_db_connection()
    cursor = conn.cursor()

    # Запрос на получение расписания
    cursor.execute("SELECT * FROM raspisanie624")  # Замените на ваш запрос
    schedule_data = cursor.fetchall()

    # Закрытие соединения
    cursor.close()
    conn.close()
    schedule_data = schedule_data[::-1]

    return render_template('rasp.html', schedule=schedule_data)

if __name__ == '__main__':
    app.run(debug=True)