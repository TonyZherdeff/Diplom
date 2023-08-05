from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
username = ''
message = ''


@app.route('/')
def start():
    return render_template('start.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    global username
    global message
    password = ''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(id INT PRIMARY KEY, login TEXT, password TEXT);""")
    con.commit()
    cur.execute("""SELECT login, password FROM users""")
    check_login_password = cur.fetchall()
    log_pas = [username, password]
    l_p = tuple(log_pas)
    if l_p in check_login_password and username and password:
        return redirect(url_for('index_l'), 302)
    elif not username and not password:
        message = "Поля Логин и Пароль не должны быть пустыми"
    elif not username:
        message = "Поле Логин пустое, повторите попытку"
    elif not password:
        message = "Поле Пароль пустое, повторите попытку"
    else:
        message = "Пользователь с таким именем и (или) паролем не существует"
    return render_template('login.html', message=message, username=username)


@app.route('/auth_bad', methods=['POST', 'GET'])
def auth():
    global username
    global message
    password = ''
    check_log_list = []
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(id INT PRIMARY KEY, login TEXT, password TEXT);""")
    con.commit()
    cur.execute("""SELECT login FROM users""")
    check_login = cur.fetchall()
    for i in check_login:
        for j in i:
            if j not in check_log_list:
                check_log_list.append(j)
    i_d = len(check_log_list)
    if username not in check_log_list and username and password:
        cur.execute("""INSERT INTO users VALUES (?, ?, ?)""", (i_d, username, password))
        con.commit()
        return redirect(url_for('index_l'), 302)
    elif not username and not password:
        message = "Поля Логин и Пароль не должны быть пустыми"
    elif not username:
        message = "Поле Логин пустое, повторите попытку"
    elif not password:
        message = "Поле Пароль пустое, повторите попытку"
    else:
        message = "Пользователь с таким именем уже существует"
    return render_template('auth.html', message=message, username=username)


@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/home_l')
def index_l():
    global username
    return render_template('index_l.html', username=username)


@app.route('/JohnBio', methods=['POST', 'GET'])
def john_bio():
    return render_template('john_bio.html')


@app.route('/PaulBio', methods=['POST', 'GET'])
def paul_bio():
    return render_template('paul_bio.html')


@app.route('/RingoBio', methods=['POST', 'GET'])
def ringo_bio():
    return render_template('ringo_bio.html')


@app.route('/GeorgeBio', methods=['POST', 'GET'])
def george_bio():
    return render_template('george_bio.html')


@app.route('/JohnBio_l', methods=['POST', 'GET'])
def john_bio_l():
    global username
    return render_template('john_bio_l.html', username=username)


@app.route('/PaulBio_l', methods=['POST', 'GET'])
def paul_bio_l():
    global username
    return render_template('paul_bio_l.html', username=username)


@app.route('/RingoBio_l', methods=['POST', 'GET'])
def ringo_bio_l():
    global username
    return render_template('ringo_bio_l.html', username=username)


@app.route('/GeorgeBio_l', methods=['POST', 'GET'])
def george_bio_l():
    global username
    return render_template('george_bio_l.html', username=username)


@app.route('/PleasePleaseMe', methods=['POST', 'GET'])
def please_please_me():
    global username
    return render_template('Please_Please_Me.html', username=username)


@app.route('/WithTheBeatles', methods=['POST', 'GET'])
def with_the_beatles():
    global username
    return render_template('With_the_Beatles.html', username=username)


@app.route('/AHardDaysNight', methods=['POST', 'GET'])
def a_hard_days_night():
    global username
    return render_template('A_Hard_Days_Night.html', username=username)


@app.route('/BeatlesForSale', methods=['POST', 'GET'])
def beatles_for_sale():
    global username
    return render_template('Beatles_For_Sale.html', username=username)


@app.route('/Help', methods=['POST', 'GET'])
def help_():
    global username
    return render_template('Help.html', username=username)


@app.route('/RubberSoul', methods=['POST', 'GET'])
def rubber_soul():
    global username
    return render_template('Rubber_Soul.html', username=username)


@app.route('/Revolver', methods=['POST', 'GET'])
def revolver():
    global username
    return render_template('Revolver.html', username=username)


@app.route('/Pepper', methods=['POST', 'GET'])
def pepper():
    global username
    return render_template('Pepper.html', username=username)


@app.route('/MagicalMysteryTour', methods=['POST', 'GET'])
def magical_mystery_tour():
    global username
    return render_template('Magical_Mystery_Tour.html', username=username)


@app.route('/TheBeatles', methods=['POST', 'GET'])
def the_beatles():
    global username
    return render_template('The_Beatles.html', username=username)


@app.route('/YellowSubmarine', methods=['POST', 'GET'])
def yellow_submarine():
    global username
    return render_template('Yellow_Submarine.html', username=username)


@app.route('/AbbeyRoad', methods=['POST', 'GET'])
def abbey_road():
    global username
    return render_template('Abbey_Road.html', username=username)


@app.route('/LetItBe', methods=['POST', 'GET'])
def let_it_be():
    global username
    return render_template('Let_It_Be.html', username=username)


if __name__ == "__main__":
    app.run(debug=True)
