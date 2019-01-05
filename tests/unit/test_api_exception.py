import pytest
import tasks

def test_add_raise():
    """add() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.add(task='not a task object')

def test_start_tasks_db_raises():
    """Make sure unsupported db raises an exception"""
    with pytest.raises(ValueError) as excinfo:
        tasks.start_tasks_db('some/grewat/path','mysql')

    excetion_msg= excinfo.value.args[0]
    assert  excetion_msg == "db_type must be a 'tiny' or 'mongo'"