import pytest
import tasks


@pytest.mark.smoke
def test_list_raises():
    """list() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.list_tasks(owner='test')




@pytest.mark.smoke
@pytest.mark.smoke1
def test_get_raises():
    """get()should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.get(taks_id='123')