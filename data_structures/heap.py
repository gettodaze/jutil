from __future__ import annotations

import heapq  # for reference
import typing as tp
from unicodedata import name

K = tp.TypeVar("K")


class _HeapElement(tp.NamedTuple, tp.Generic[K]):
    el: K
    key: tp.Any = None


class MinHeap(tp.Generic[K]):
    def __init__(
        self,
        *,
        key: tp.Callable[[K], tp.Any] | None = None,
        max_size: int | None = None,
    ) -> None:
        self.arr: list[_HeapElement[K]] = []
        self.key = key
        self.max_size = None

    @staticmethod
    def get_parent_idx(idx: int) -> int | None:
        assert idx >= 0
        if idx == 0:
            return None
        if idx % 2:
            return (idx - 1) // 2
        return (idx - 2) // 2

    @staticmethod
    def get_left_idx(idx: int) -> int:
        return idx * 2 + 1

    def __repr__(self) -> str:
        el_str = ", ".join(str(x.el) for x in self.arr)
        return f"{self.__class__.__name__}([{el_str}])"

    def __bool__(self) -> bool:
        return bool(self.arr)

    def push(self, el: K):
        if self.max_size is not None and len(self.arr) >= self.max_size:
            raise RuntimeError(f"Heap is full. {len(self.arr)=} >= {self.max_size=}")

        # append
        compare = self.key(el) if self.key else el
        cur_idx = len(self.arr)
        self.arr.append(_HeapElement(el, compare))
        parent_idx = self.get_parent_idx(cur_idx)

        # bubble up
        while parent_idx:
            if self.arr[parent_idx].key <= compare:
                break
            # fmt: off
            self.arr[parent_idx], self.arr[cur_idx] = self.arr[cur_idx], self.arr[parent_idx]
            # fmt: on
            cur_idx = parent_idx
            parent_idx = self.get_parent_idx(parent_idx)

    def pop(self) -> K:
        if not self.arr:
            raise RuntimeError("Cannot pop empty heap")
        if len(self.arr) == 1:
            return self.arr.pop()

        ret = self.arr[0]
        self.arr[0] = self.arr.pop()
        cur_idx, child_idx = 0, 1
        N = len(self.arr)

        # bubble down
        while child_idx < N:
            if (
                child_idx + 1 < N
                and self.arr[child_idx + 1].key < self.arr[child_idx].key
            ):
                child_idx += 1

            if self.arr[cur_idx].key < self.arr[child_idx].key:
                break

            # fmt: off
            self.arr[child_idx], self.arr[cur_idx] = self.arr[cur_idx], self.arr[child_idx]
            # fmt: on
            cur_idx = child_idx
            child_idx = self.get_left_idx(child_idx)

        return ret.el


if __name__ == "__main__":
    import IPython

    h = MinHeap()
    for x in [1, 9, 2, 7, 5, 4, 3, 4]:
        h.push(x)
    print(h)
    while h:
        print(h.pop())
    IPython.embed()
