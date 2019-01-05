import pytest
import tasks
from tasks import Task


class TestUpdate():
    """Test expected exceptions with tasks.update()."""


    def test_bad_id(self):
        """A non-int id should raise an exception."""
        with pytest.raises(TypeError):
            tasks.update(task_id={'dict instead': 1},
                         task=tasks.Task())

    def test_bad_task(self):
        """A non-Task task should raise an exception"""
        with pytest.raises(TypeError):
            tasks.update(task_id=1, task='not a task')

@pytest.fixture(autouse=True)
def initialized_task_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    # Setup : start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    # Teardown: stop db
    yield  # this is where the testing happens
    tasks.stop_tasks_db()

@pytest.mark.userfixtures('tasks_db')
class TestAdd():
    def test_missing_summary(self):
        """Should raise an exception if summary missing."""
        with pytest.raises(ValueError):
            tasks.add(Task(owner='bob'))


    def test_done_not_bool(self):
        """Should raise an exception if done is not a bool."""
        with pytest.raises(ValueError):
            tasks.add(Task(summary ='summary',done = 'True'))