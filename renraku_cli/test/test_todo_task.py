from renraku_cli.core import todo_task


def test_get_task():
    result = todo_task.get_task(1)
    assert result == {
        "id": 1,
        "title": "First task",
        "description": "Some description",
        "completed": True,
    }


def test_get_all_tasks():
    result = todo_task.get_all_tasks()
    assert len(result) > 1
