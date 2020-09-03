# !/usr/bin/python
# -*- coding:utf-8 -*-
# p_cascade_map = {
#     0: [{'n_id': 1, 'vc_name': '湖州中院'}, {'n_id': 21, 'vc_name': '温州中院'}, {'n_id': 23, 'vc_name': '湖州市中级人民法院'}],
#     1: [{'n_id': 11, 'vc_name': '中院'}, {'n_id': 12, 'vc_name': '德清法院'}, {'n_id': 24, 'vc_name': '南浔法院'},
#         {'n_id': 25, 'vc_name': '吴兴法院'}, {'n_id': 26, 'vc_name': '长兴法院'}, {'n_id': 27, 'vc_name': '安吉法院'},
#         {'n_id': 34, 'vc_name': '南太湖法院'}, {'n_id': 57, 'vc_name': 'string'}],
#     11: [{'n_id': 13, 'vc_name': '长兴法院'}, {'n_id': 14, 'vc_name': '安吉法院'}, {'n_id': 15, 'vc_name': '吴兴法院'},
#          {'n_id': 16, 'vc_name': '南浔法院'}],
#     16: [{'n_id': 22, 'vc_name': '坐席部门'}]}


p_cascade_map = {
    0: [{'n_id': 1, }, {'n_id': 2, }, {'n_id': 3, }, {'n_id': 9}],
    1: [{'n_id': 4, }, {'n_id': 5, }],
    3: [{'n_id': 7, }],
}


def _dept_iter(p_cascade_map, p_key):
    dept_iter_list = p_cascade_map.pop(p_key, [])
    for dept in dept_iter_list:
        if p_cascade_map.get(dept['n_id']):
            child_list = _dept_iter(p_cascade_map, dept['n_id'])
            if len(child_list) > 0:
                dept['childs'] = child_list
    return dept_iter_list


dept_iter_list = _dept_iter(p_cascade_map, 0)
print(dept_iter_list)
