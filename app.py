from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

# Database Configuration
db = pymysql.connect(
    host='sql11.freesqldatabase.com',
    user='sql11653855',
    password='x2lIMdfC7C',
    database='sql11653855',
    port=3306
)

@app.route('/')
def index():
    cursor = db.cursor()
    cursor.execute('SELECT content FROM pastes ORDER BY created_at DESC')
    pastes = cursor.fetchall()
    cursor.close()
    return render_template('index.html', pastes=pastes)


@app.route('/add_paste', methods=['POST'])
def add_paste():
    content = request.form['content']
    cursor = db.cursor()
    cursor.execute('INSERT INTO pastes (content) VALUES (%s)', (content,))
    db.commit()
    cursor.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
