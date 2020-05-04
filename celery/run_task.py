from proj.tasks import add
from proj.celery import app

id = add.delay(2, '2').id
print("ID:", type(id), id)
res = app.AsyncResult(id)
print("RESULT:", res.get(timeout=1, propagate=False))
print("STATE:", res.state)
print("TRACEBACK ------")
print(res.traceback)

