import json
import os
import idgen


# Todo の一覧を表示する
def list():
    todos = restore_todos()
    for x in todos:
        checkmark = "☑" if x["completed"] else "  "
        print("{0} [{1}]    {2}".format(checkmark, x["id"], x["subject"]))


# Todo を追加する
def add(subject):
    todos = restore_todos()
    new_todo = {
        "subject": subject,
        "id": idgen.generate_id(),
        "completed": False
    }
    todos.append(new_todo)
    with open("./todo.json", 'w') as json_file:
        # ensure_ascii が True になっていると
        # 日本語などがエスケープされる
        json.dump(todos, json_file, indent=4, ensure_ascii=False)


# Todo を完了する
def complete(todo_id):
    todos = restore_todos()
    a = [x for x in todos if x["id"] == todo_id]
    if len(a) > 0:
        todo_to_complete = a[0]
        todo_to_complete["completed"] = True
        with open("./todo.json", 'w') as json_file:
            json.dump(todos, json_file, indent=4, ensure_ascii=False)
    else:
        print("ID に相当する Todo が存在しません: " + todo_id)


# Todo を保存しているJSONのテキストからPythonのオブジェクトに復元する
def restore_todos():
    if os.path.exists("./todo.json"):
        with open("./todo.json", 'r') as json_file:
            json_data = json.loads(json_file.read())
            return json_data
    else:
        return []
