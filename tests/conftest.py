"""Placeholder."""

# nothing here yet
import pytest
import tasks
from tasks import Task
from selenium import webdriver


@pytest.fixture()
def tasks_db(tmpdir):
    """Connect to db before tests , disconnet after."""
    # Setup: start tasks_db
    tasks.start_tasks_db(str(tmpdir),'tiny')
    yield # this is where the testing happens
    # Teardown : stop db
    tasks.stop_tasks_db()

# Reminder of Task constructor interface
# Task(summary = None, owner = None, done = False, id= None)
# summary is required
# owner and done are optioal
# id is set by databae

@pytest.fixture()
def tasks_just_a_few():
    """All summaries and owners are unique"""
    return(
        Task('Write some code', 'Brian', True),
        Task("code reviewe Brian's code", 'Katie', False),
        Task('Fix what Brian did', 'Michelle', False)
    )

@pytest.fixture()
def tasks_mult_per_owner():
    """Several owners with several tasks each"""
    return(
        Task('make a cookie', 'Brian', True),
        Task("use a emoji", 'Katie', False),
        Task('move to Berlin', 'Michelle', False),
        Task('create', 'Michelle', False),
        Task('Inspier', 'Michelle', False),
        Task('Encourage', 'Michelle', False),
        Task('Fix what Brian did', 'Michelle', False),
    )

@pytest.fixture()
def db_with_3_tasks(tasks_db, tasks_just_a_few):
    """Connected db with 3 tasks, all unique"""
    for t in tasks_just_a_few:
        tasks.add(t)
@pytest.fixture()
def db_with_multi_per_owner(taks_db, tasks_mult_per_owner):
    """conected db with 9 tasks, 3 owerners, all with 3 tasks"""
    for t in tasks_mult_per_owner:
        tasks.add(t)


def pytest_report_header():
    """Thank tester for running tests"""
    return "Thaks for running the tests."

def pytest_report_teststatus(report):
    """Turn failures into opportunities."""
    if report.when == 'call' and report.failed:
        return(report.outcome, 'o', 'OPPORTUNITY for improvedment')

