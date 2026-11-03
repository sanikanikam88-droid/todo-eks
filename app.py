from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)
tasks = []  # simple in-memory list

PAGE = """
<h1>My To-Do List v1</h1>
<form method="post" action="/add">
  <input name="title" placeholder="New task" required>
  <button>Add</button>
</form>
<ul>
{% for t in tasks %}
  <li>{{ '✅' if t.done else '⬜' }} {{ t.title }}
    <a href="/done/{{ loop.index0 }}">[done]</a>
    <a href="/delete/{{ loop.index0 }}">[delete]</a></li>
{% endfor %}
</ul>
"""


class Task:
    def __init__(self, title):
        self.title = title
        self.done = False


@app.route("/")
def index():
    return render_template_string(PAGE, tasks=tasks)


@app.route("/add", methods=["POST"])
def add():
    tasks.append(Task(request.form["title"]))
    return redirect("/")


@app.route("/done/<int:i>")
def done(i):
    if 0 <= i < len(tasks):
        tasks[i].done = True
    return redirect("/")


@app.route("/delete/<int:i>")
def delete(i):
    if 0 <= i < len(tasks):
        tasks.pop(i)
    return redirect("/")


@app.route("/health")
def health():
    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
