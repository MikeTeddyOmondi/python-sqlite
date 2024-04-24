# Imports
import inspect
from models import Base, Todo
from db import engine, session
from sqlalchemy import select, update

# Create Tables
Base.metadata.create_all(engine)

# Insert to DB
# session.add(Todo(title='todo one'))
# session.commit()

# Select all from DB
# -------------------------------------
select_all_query = session.query(Todo)
# print(select_all_query)
results = []

for todo in select_all_query:
    # print(todo._asdict())
    results.append(todo._asdict())

nrows = len(results)
print(results)
print(nrows)

# Select one from DB
# -------------------------------------
select_one_query = session.query(Todo).filter_by(id=1)
# print(select_one_query)
for todo in select_one_query:
    print(todo._asdict())

# Update one from DB
# -------------------------------------
# engine.execute('UPDATE todos SET title = ? WHERE id = ?', "Updated title three", 3)
# session.execute(update(Todo).where(Todo.id == 3), params=Todo(title="Updated"))
todo = session.query(Todo).filter_by(id=3).first()
todo.title = "Title three updated"
session.commit()

# Delete one from DB
# -------------------------------------
# query = session.query(Todo).filter_by(id=1)
# object_instance = query.first()
# session.delete(object_instance)
# session.commit()

# select_all_query = session.query(Todo)
# results = []

# for todo in select_all_query:
#     # print(todo._asdict())
#     results.append(todo._asdict())

# nrows = len(results)
# # print(results)
# print(nrows)
