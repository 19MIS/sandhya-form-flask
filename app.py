from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Database connection
conn = sqlite3.connect('submissions.db')
c = conn.cursor()

# Create submissions table
c.execute('''CREATE TABLE IF NOT EXISTS submissions
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL,
              email TEXT NOT NULL)''')
conn.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    # Insert submission into database
    c.execute("INSERT INTO submissions (name, email) VALUES (?, ?)", (name, email))
    conn.commit()

    return 'Submission successful'

if __name__ == '__main__':
    app.run(debug=True)
