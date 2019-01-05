import _pytest
import pytest
import tasks
from tasks import Task


@pytest.fixture(autouse=True)
def initialized_task_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    # Setup : start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    # Teardown: stop db
    yield  # this is where the testing happens
    tasks.stop_tasks_db()

@pytest.mark.skip(reason='misunderstood the API')
def test_unique_id():
    """calling unique_id() twice should return diffeent numbers."""
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2

def test_unique_id_2():
    """unique_id should return an unused id."""
    ids = [tasks.add(Task('one')), tasks.add(Task('tow')), tasks.add(Task('three'))]
    # grab a unique id
    uid = tasks.unique_id()
    print("uid is   " + ":" + uid.__str__())
    # make sure it isn't in the List of existing ids
    assert uid not in ids
