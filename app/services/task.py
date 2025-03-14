import threading
import uuid
from app.core.sqlite_cache import db_cache
from app.core.task_generator import TASK_GENERATOR


DEFAULT_HTML = (
    """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Task Generator</title>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <p>This is a default HTML response.</p>
        </body>
    </html>
    """
)


lock = threading.Lock()


@db_cache
def cached_get_seed(session:int, task_number:int):
    seed = session * (task_number + 5)
    task_id_seed = str(uuid.uuid4())
    return seed, task_id_seed


@db_cache
def cached_get_task(session:int, task_number:int):
    task = TASK_GENERATOR.get_task()
    return task.html if task is not None else DEFAULT_HTML

def get_seed(session:int, task_number:int):
    with lock:
        seed, task_id_seed = cached_get_seed(session, task_number)
    return seed, task_id_seed


def get_task(session:int, task_number:int):
    with lock:
        task = cached_get_task(session, task_number)
    return task