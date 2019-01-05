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


def test_add_returns_valid_id():
    """tasks.add(<valid task>)should return an integer."""
    # Given an initialized tasks db
    # when a new task is added
    # then returned task_id is of type int
    new_task = Task('do something')
    task_id = tasks.add(new_task)
    print("id is" +task_id.__str__())
    assert isinstance(task_id, int)


@pytest.mark.smoke
def test_add_taks_has_id_set():
    """Make sure the task_id field is set by tasks.add()."""
    # given an intialized tasks db
    # Add a new task is added

    new_task = Task('sit in chair', owner='me', done=True)
    task_id = tasks.add(new_task)

    # when task is retrived
    task_from_db = tasks.get(task_id)

    # then task_id matches id field
    assert task_from_db.id == task_id
