# celery-getting-started
trial celery getting started

## multi return

can use collect?

https://docs.celeryproject.org/en/latest/reference/celery.result.html#celery.result.AsyncResult.collect

## terminate task

can use revoke?

https://docs.celeryproject.org/en/latest/userguide/workers.html#revoke-revoking-tasks

## stop and restart client

task can be recovered from (result).id `res = app.AsynResult(id)`

https://docs.celeryproject.org/en/latest/userguide/calling.html

https://docs.celeryproject.org/en/latest/reference/celery.result.html#celery.result.AsyncResult

## remote client

https://docs.celeryproject.org/en/latest/getting-started/next-steps.html#canvas-designing-work-flows

celery -A proj inspect registered

user incomplete remote worker signature?

https://docs.celeryproject.org/en/latest/reference/celery.html?highlight=Celery#celery.signature

app.signature('proj.tasks.add')

## result consume backend resource

https://docs.celeryproject.org/en/latest/userguide/tasks.html#task-result-backends

> Backends use resources to store and transmit results. To ensure that resources are released, you must eventually call get() or forget() on EVERY AsyncResult instance returned after calling a task. 

https://docs.celeryproject.org/en/latest/userguide/tasks.html#ignore-results-you-don-t-want

use decorater argument
> @app.task(ignore_result=True)