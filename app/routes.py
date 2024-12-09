from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__)

tasks = []  # Temporary storage for tasks

@main.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@main.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append({'task': task, 'completed': False})
    return redirect(url_for('main.index'))

@main.route('/complete/<int:task_id>')
def complete_task(task_id):
    tasks[task_id]['completed'] = True
    return redirect(url_for('main.index'))

@main.route('/delete/<int:task_id>')
def delete_task(task_id):
    tasks.pop(task_id)
    return redirect(url_for('main.index'))
