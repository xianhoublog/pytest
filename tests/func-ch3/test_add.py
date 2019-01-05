import pytest
import tasks
from tasks import Task

@pytest.mark.nannantest
def test_add_increases_count(db_with_3_tasks):
    """Test tasks.add() affect on tasks.count()"""
    # GIVEN a db with 3 tasks
    # When another tasks is added
    tasks.add(Task('throw a party'))
    # Then the count increases by 1
    assert tasks.count() ==4