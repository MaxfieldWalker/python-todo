import sys
import todo

if len(sys.argv) >= 3:
    [_, subcommand, arg] = sys.argv
    if subcommand == "add":
        todo.add(arg)
    elif subcommand == "complete":
        todo.complete(arg)
else:
    todo.list()
