# celery-getting-started
trial celery getting started

## multi return

can use collect?

https://docs.celeryproject.org/en/latest/reference/celery.result.html#celery.result.AsyncResult.collect

## terminate task

can use revoke?

https://docs.celeryproject.org/en/latest/userguide/workers.html#revoke-revoking-tasks

## stop and restart client

task can be recovered from (result).id?
https://docs.celeryproject.org/en/latest/userguide/calling.html
https://docs.celeryproject.org/en/latest/reference/celery.result.html#celery.result.AsyncResult

## remote client

can make incomplete signature

https://docs.celeryproject.org/en/latest/getting-started/next-steps.html#canvas-designing-work-flows

celery -A proj inspect registered

can make incomplete remote worker signature?

https://docs.celeryproject.org/en/latest/reference/celery.html?highlight=Celery#celery.signature

app.signature('proj.tasks.add')

