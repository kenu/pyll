import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import redis

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Redis configuration
redis_client = redis.Redis(host='redis', port=6379, db=0)
try:
    redis_client.ping()
    print("Successfully connected to Redis!")
except redis.exceptions.ConnectionError as e:
    print(f"Could not connect to Redis: {e}")


# Todo model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)

    def __repr__(self):
        return f'<Todo {self.id}>'

@app.route('/')
def index():
    with app.app_context():
        todos = Todo.query.all()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    with app.app_context():
        todo = Todo(text=request.form['todoitem'], complete=False)
        db.session.add(todo)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:todo_id>')
def update(todo_id):
    with app.app_context():
        todo = Todo.query.get_or_404(todo_id)
        todo.complete = not todo.complete
        db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    with app.app_context():
        todo = Todo.query.get_or_404(todo_id)
        db.session.delete(todo)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=8000)
