import pytest
import tasks
from tasks import Task

def test_add_returns_valid_id():
    """tasks.add(<valid task>)should return an integer."""
    # Given an initialized tasks db
    # when a new task is added
    # then returned task_id is of type int
    new_task = Task('do something')
    task_id = tasks.add(new_task)
    print("id is" +task_id.__str__())
    assert isinstance(task_id, int)


@pytest.fixture()
def a_tuple():
    """return something more interesting."""
    return(1, 'foo', None, {'bar' :23})
def test_a_tuple(a_tuple):
    """Demo the a_tuple fixture"""
    assert a_tuple[3]['bar'] == 23

