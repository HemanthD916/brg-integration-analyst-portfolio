from flask import Flask, render_template, request, redirect, url_for
from library import Library

app = Flask(__name__)
library = Library()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'POST':
        # Handle add/edit/delete based on form
        action = request.form['action']
        if action == 'add':
            try:
                book_id = int(request.form['book_id'])
                cost = float(request.form['cost'])
                library.books.add_book(Book(request.form['author'], request.form['title'], request.form['isbn'], book_id, cost))
            except ValueError:
                pass  # Handle error in template
        # Similar for edit/delete
    return render_template('books.html', books=library.books.books.values())

# Add similar routes for /patrons, /loans

if __name__ == '__main__':
    app.run(debug=True)
