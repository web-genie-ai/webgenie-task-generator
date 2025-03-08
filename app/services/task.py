import threading
import uuid
from app.core.sqlite_cache import db_cache
from app.core.task_generator import TASK_GENERATOR

lock = threading.Lock()


@db_cache
def cached_get_seed(session:int, task_number:int):
    seed = session * (task_number + 5)
    task_id_seed = str(uuid.uuid4())
    return seed, task_id_seed


def get_seed(session:int, task_number:int):
    with lock:
        seed, task_id_seed = cached_get_seed(session, task_number)
    return seed, task_id_seed


def get_task():
    return TASK_GENERATOR.get_task()