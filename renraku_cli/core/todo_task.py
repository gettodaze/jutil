import typing as tp

import requests
from renraku_cli.core.config import User, task_user

JSON = tp.Dict[str, tp.Any]
BASE_URL = "http://127.0.0.1:8000/todo/api"


def _call_endpoint(endpoint: str, method: str = "get", **kwargs) -> JSON:
    url = BASE_URL + endpoint
    resp = requests.request(method, url, **kwargs)
    resp.raise_for_status()
    return resp.json()


def get_task(task_id: int) -> JSON:
    return _call_endpoint(f"/todos/{task_id}")


def get_all_tasks() -> JSON:
    return _call_endpoint("/todos")


def post_task(
    title: str,
    user: User = task_user,
    description: str = "",
    completed: bool = False,
) -> JSON:
    data = dict(title=title, description=description, completed=completed)
    return _call_endpoint(
        "/todos/", method="post", data=data, auth=(user.username, user.password)
    )


if __name__ == "__main__":
    from IPython import embed

    embed()
