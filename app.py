from flask import *
import pymongo
from bson.objectid import ObjectId

app = Flask(__name__, static_folder = 'public', static_url_path = '/')
app.secret_key = 'abcxyz'


uri = "mongodb+srv://todos:todos123@mycluster.j02eof1.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)
db = client.todolist_system
todos_collection = db.todos



@app.route('/')
def index():
    todos = todos_collection.find()
    return render_template('index2.html', items = todos)



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