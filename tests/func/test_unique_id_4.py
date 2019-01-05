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

@pytest.mark.xfail(tasks.__version__<'0.2.0', reason = 'not supported unitla version 0.2.0')
def test_unique_id():
    """calling unique_id() twice should return diffeent numbers."""
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2

@pytest.mark.xfail()
def test_unique_id_is_a_duck():
    """Demostrate xfail"""
    uid = tasks.unique_id()
    assert uid == 'a duck'

@pytest.mark.xfail()
def test_unique_id_not_a_duck():
    "Demostrate xpass"
    uid = tasks.unique_id()
    assert uid != 'a duck'