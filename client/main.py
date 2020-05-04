from celery import Celery

app = Celery('client',
             broker='redis://redis',
             backend='redis://redis')
add = app.signature("proj.tasks.add")


def run(a, b):
    print("ARG1:", type(a), a)
    print("ARG2:", type(b), b)
    id = add.delay(a, b).id
    print("ID:", type(id), id)
    res = app.AsyncResult(id)
    print("RESULT:", res.get(timeout=1, propagate=False))
    print("STATE:", res.state)
    print("TRACEBACK ------")
    print(res.traceback)


if __name__ == '__main__':
    run(2, 2)
    run(2, '2')

