# !/usr/bin/python
# -*- coding:utf-8 -*-
from collections import defaultdict, deque

id_pairs = {
    (0, 1), (0, 2), (0, 3),
    (1, 4), (1, 5),
    (2, 7),
    (4, 8), (4, 9), (4, 10),
    (7, 11),
}

x = {0: {1, 2, 3},
     2: {7},
     1: {4, 5},
     4: {7, 8, 9}
     }


# 就算 0下面包含什么


def sub_rel_reformer(id_pairs, max_deep=10):
    sub_rel = defaultdict(set)
    for sup_id, id in id_pairs:
        sub_rel[sup_id].add(id)
    all_sub_rel = defaultdict(set)
    deep_limit = max_deep - 1
    for k, sub_ids in sub_rel.items():
        id_stack = []
        id_stack.append(k)
        sub_all_id = set()
        deep_counter = 0

        while len(id_stack) > 0:
            if deep_counter > deep_limit:
                break
            s_id = id_stack.pop()
            for sub_id in sub_rel.get(s_id, set()):
                sub_all_id.add(sub_id)
                id_stack.append(sub_id)
            deep_counter += 1

        all_sub_rel[k] = sub_all_id
    return {k: list(v) for k, v in all_sub_rel.items()}


print(sub_rel_reformer(id_pairs, max_deep=10))
