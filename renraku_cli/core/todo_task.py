from __future__ import annotations

import typing as tp

import requests
from renraku_cli.core.config import User, task_user

JSON = tp.Dict[str, tp.Any]
BASE_URL = "http://127.0.0.1:8000/todo/api"

TITLE = "title"
DESCRIPTION = "description"
COMPLETED = "completed"
TASK_ID = "id"


class Task(tp.NamedTuple):
    title: str
    description: str
    completed: bool
    task_id: int

    @classmethod
    def from_json(cls, json: dict) -> Task:
        json["task_id"] = json.pop(TASK_ID)
        return cls(**json)


def _call_endpoint(endpoint: str, method: str = "get", **kwargs) -> JSON:
    url = BASE_URL + endpoint
    print(f"{method.upper():<10} {url}\n{kwargs}\n")
    resp = requests.request(method, url, **kwargs)
    resp.raise_for_status()
    return resp.json()


def get_task(task_id: int) -> Task:
    json = _call_endpoint(f"/todos/{task_id}")
    return Task.from_json(json)


def get_all_tasks() -> tuple[Task, ...]:
    json = _call_endpoint("/todos")
    return tuple(Task.from_json(el) for el in json)


def post_task(
    title: str,
    user: User = task_user,
    description: str = "",
    completed: bool = False,
) -> Task:
    data = dict(title=title, description=description, completed=completed)
    json = _call_endpoint(
        "/todos/", method="post", data=data, auth=(user.username, user.password)
    )
    return Task.from_json(json)


def update_task(
    task_id: int,
    title: str | None = None,
    description: str | None = None,
    completed: bool | None = None,
    user: User = task_user,
) -> Task:
    items = [(TITLE, title), (DESCRIPTION, description), (COMPLETED, completed)]
    data = {k: v for k, v in items if v is not None}
    if not data:
        raise ValueError("Must specify one item")

    # need to figure out how to make title optional in put requests
    if title is None:
        data[TITLE] = get_task(task_id).title

    json = _call_endpoint(
        f"/todos/{task_id}/",
        method="put",
        json=data,
        auth=(user.username, user.password),
    )
    return Task.from_json(json)


if __name__ == "__main__":
    from IPython import embed

    embed()
