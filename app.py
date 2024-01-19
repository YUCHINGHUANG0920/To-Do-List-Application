from flask import *
import pymongo
from bson.objectid import ObjectId

app = Flask(__name__, static_folder = 'public', static_url_path = '/')
app.secret_key = 'abcxyz'


### input the personal URI to connect to a MongoDB database hosted on the MongoDB Atlas cloud service
# uri = "The string is a connection URI (Uniform Resource Identifier)"

### create a MongoDB client object (client) using the pymongo library in Python
# client = pymongo.MongoClient(uri)

### create a variable named db to represent the MongoDB database (todolist_system)
# db = client.todolist_system

### creates a variable named todos_collection to represent todos (the name of a collection within the todolist_system database)
# todos_collection = db.todos



@app.route('/')
def index():
    todos = todos_collection.find()
    return render_template('index.html', items = todos)



@app.route('/add', methods = ['POST'])
def add():
    title = request.form.get("title")
    new_todo = {"title": title, "complete": False}
    todos_collection.insert_one(new_todo)

    return redirect(url_for('index'))



@app.route('/update/<string:todo_id>', methods = ['GET', 'POST'])
def update(todo_id):
    todo = todos_collection.find_one({"_id": ObjectId(todo_id)})
    if todo:
        new_value = not todo["complete"]
        todos_collection.update_one({"_id": ObjectId(todo_id)}, {"$set": {"complete": new_value}})

    return redirect(url_for('index'))



@app.route('/delete/<string:todo_id>',  methods = ['GET', 'POST'])
def delete(todo_id):
    todos_collection.delete_one({"_id": ObjectId(todo_id)})
    
    return redirect(url_for('index'))



app.run(port = 3000)