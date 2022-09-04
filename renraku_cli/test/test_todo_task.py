from renraku_cli.core import todo_task


def test_get_task():
    result = todo_task.get_task(1)
    expected = todo_task.Task(
        title="First task", description="Update", completed=True, task_id=1
    )
    assert result == expected


def test_get_all_tasks():
    result = todo_task.get_all_tasks()
    assert len(result) > 1
