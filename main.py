from flask import Flask, request, redirect
import cgi
import os
import jinja2

# Set up jinja environment
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

# Set up Flask application
app = Flask(__name__)
app.config['DEBUG'] = True

# Use a global variable to store tasks (until we learn about databases)
tasks = []


@app.route('/')
def index():
    """
    You always need a root route to make things easy for customers
    But it just needs to take us to the todo functionality shown in the videos
    """
    return redirect('/todos')

@app.route('/todos', methods=['POST', 'GET'])
def todos():
    """
    If we get a new task (a POST), add it to the list
    then (or only, if we are responding to a GET)
    Render the list of tasks using Jinja!!
    """
    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)

    template = jinja_env.get_template('todos.html')
    return template.render(title="TODOs", tasks=tasks)

app.run()
