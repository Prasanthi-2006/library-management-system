from flask import Flask, render_template, request, redirect
from datetime import datetime, timedelta
import os  # 🔁 Import os to read the PORT variable from the environment

app = Flask(__name__)

# Sample data
books = {
    "Python Basics": {"author": "John Zelle", "total": 5, "available": 2},
    "Data Structures": {"author": "Mark Allen", "total": 5, "available": 3},
    "Machine Learning": {"author": "Tom Mitchell", "total": 5, "available": 4},
    "Operating Systems": {"author": "Abraham Silberschatz", "total": 5, "available": 5},
    "Computer Networks": {"author": "Andrew S. Tanenbaum", "total": 5, "available": 1}
}

issued_books = [
    {"name": "Prathyusha", "id": "24BK1A05F0", "book": "Python Basics", "due": "21/07/2025"},
    {"name": "Amitha", "id": "24BK1A05F7", "book": "Data Structures", "due": "22/07/2025"},
    {"name": "Shalini", "id": "24BK1A05E2", "book": "Machine Learning", "due": "25/07/2025"},
    {"name": "Reena", "id": "24BK1A66G6", "book": "Computer Networks", "due": "28/07/2025"}
]

@app.route('/')
def home():
    return render_template("index.html", books=books, issued_books=issued_books)

@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    total = int(request.form['total'])
    books[title] = {"author": author, "total": total, "available": total}
    return redirect('/')

# 🔁 FIX THIS PART
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # default to 5000 if PORT is not set
    app.run(host='0.0.0.0', port=port, debug=True)
