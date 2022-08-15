from data_structures import heap


def test_heap():
    h = heap.MinHeap()
    values = [1, 9, 2, 7, 5, 4, 3, 4, -2, 7]
    for x in values:
        h.push(x)

    result = []
    while h:
        result.append(h.pop())

    assert sorted(values) == result
