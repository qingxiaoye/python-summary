# !/usr/bin/python
# -*- coding:utf-8 -*-
import json

import requests


url = 'http://192.168.100.210:9910/api/v1/wkorder/add-robot'
d={"l_ref_case": [{"n_response_code": 0, "vc_business_court_contact": "string", "vc_case_code": "130320190522000001", "vc_case_number": "\uff082019\uff09\u6d590103\u53f8\u6551\u62671\u53f7", "vc_case_status": "\u5f52\u6863", "vc_clerk": "\u9ec4\u6e2d\u8389", "vc_close_case_date": "20190402", "vc_collect_case_date": "20190325", "vc_court_name": "", "vc_court_time": "", "vc_filing_date": "20190325", "vc_party_name": "\u6551\u52a9\u7533\u8bf7\u4eba:\u82cf\u5c0f\u5175", "vc_response_content": "string", "vc_response_msg": "string", "vc_response_status": "string", "vc_undertaking_court": "", "vc_undertaking_dept": "33010341", "vc_undertaking_judge": "\u5f90\u8fdc", "vc_urger_errmessage": "string", "vc_urger_id": "string", "vc_urger_result": "string", "vc_undertaker_telephone": "", "vc_court_clerk_telephone": "", "vc_subject_amount": "", "vc_collegiate_member": "", "vc_division_date": "", "vc_assistant_judge": "", "n_case_typecode": 0, "vc_case_cause": ""}], "l_ref_court": [{"vc_bus_route": "string", "vc_contact_info": "string", "vc_court_address": "string", "vc_court_name": "string", "vc_court_postcode": "string", "vc_office_hours": "string"}], "l_ref_judge": [], "l_ref_legaladvice": [], "l_ref_party": [{"vc_party_certificate": "string", "vc_party_certificate_number": "string", "vc_party_name": "string", "vc_party_sex": "string"}], "l_ref_petition": [{"is_administrative_reconsideration": 0, "is_arbitral_body_accepted": 0, "is_compound_opinion": 0, "is_court_accepted": 0, "vc_acceptance_court": "string", "vc_complainant": "string", "vc_incident_place": "string", "vc_question_category": "string"}], "n_call_time": 1598952175, "n_circulation_time": 0, "n_connect": 0, "n_connecttime0": 0, "n_connecttime1": 0, "n_drop_time": 1598952175, "n_status": 2, "o_caller_agent": {"n_age": 0, "vc_agent_name": "string", "vc_case_code": "string", "vc_certificate_number": "string", "vc_party_name": "string", "vc_phone_number": "string", "vc_sex": "string"}, "o_caller_lawyer": {"vc_competent_unit_name": "string", "vc_gender_code": "string", "vc_idcard_number": "string", "vc_law_firm_name": "string", "vc_lawyer_grade_name": "string", "vc_lawyer_license_number": "string", "vc_lawyer_name": "string", "vc_phone_number": "string", "vc_practice_name": "string"}, "o_caller_party": {"n_age": 0, "vc_address_service": "string", "vc_case_code": "string", "vc_certificate_number": "string", "vc_legal_representative": "string", "vc_litigation_status": "string", "vc_party_name": "string", "vc_party_type": "string", "vc_phone_number": "string", "vc_sex": "string"}, "vc_call_log": "", "vc_call_number": "015235394416", "vc_caller": "string", "vc_caller_type": "string", "vc_complain_user_url": "", "vc_completion_time": "string", "vc_judge_user_url": "", "vc_session_id": "1598951929.10365979", "vc_wk_caller_type_other": "string", "vc_robot_case": "\u60a8\u597d\uff0c\u60a8\u63d0\u51fa\u8bc9\u8bbc\u7684\u65e5\u671f\u5927\u6982\u662f\u4ec0\u4e48\u65f6\u5019\u5462\uff0c\u4f8b\u59822019\u5e748\u6708\uff0c&\u60a8\u597d\uff0c\u8bf7\u91cd\u65b0\u544a\u8bc9\u6211\u60a8\u53bb\u6cd5\u9662\u63d0\u51fa\u8bc9\u8bbc\u7684\u5927\u6982\u65e5\u671f\uff0c\u4f8b\u59822019\u5e748\u6708\uff0c\u60a8\u4e5f\u53ef\u4ee5\u767b\u5f55\u79fb\u52a8\u5fae\u6cd5\u9662\u6216\u6d59\u6c5f\u6cd5\u9662\u7f51\u67e5\u8be2\uff0c&\u60a8\u597d\uff0c\u8bf7\u91cd\u65b0\u544a\u8bc9\u6211\u60a8\u53bb\u6cd5\u9662\u63d0\u51fa\u8bc9\u8bbc\u7684\u5927\u6982\u65e5\u671f\uff0c\u4f8b\u59822019\u5e748\u6708\uff0c\u60a8\u4e5f\u53ef\u4ee5\u767b\u5f55\u79fb\u52a8\u5fae\u6cd5\u9662\u6216\u6d59\u6c5f\u6cd5\u9662\u7f51\u67e5\u8be2\uff0c&\u67e5\u8be2\u5230\u591a\u4e2a\u6848\u4ef6\uff0c\u6309\u7167\u6700\u65b0\u7acb\u6848\u65f6\u95f4\u64ad\u62a5\u786e\u8ba4\uff0c\u8bf7\u95ee\u6848\u53f7\u4e3a2019\u6d590103\u53f8\u6551\u62671\u53f7\uff0c\u5f53\u4e8b\u4eba\u662f\u6551\u52a9\u7533\u8bf7\u4eba\uff0c\u82cf\u5c0f\u5175\u5417\uff0c&\u8bf7\u95ee\u60a8\u8981\u67e5\u8be2\u4ec0\u4e48\u4fe1\u606f\uff0c\u60a8\u53ef\u4ee5\u67e5\u8be2\u627f\u529e\u6cd5\u9662\u3001\u6267\u884c\u6cd5\u5b98\u3001\u5f00\u5ead\u6cd5\u5ead\u3001\u5f00\u5ead\u65e5\u671f\u3001\u7acb\u6848\u65e5\u671f\u3001\u4e66\u8bb0\u5458\u3001\u6536\u6848\u65e5\u671f\u3001\u7ed3\u6848\u65e5\u671f\u3001\u627f\u529e\u90e8\u95e8\u548c\u6848\u4ef6\u72b6\u6001\uff0c&\u60a8\u597d\uff0c\u6682\u672a\u67e5\u8be2\u5230\u6848\u4ef6\u7684\u5f00\u5ead\u65e5\u671f\uff0c\u5982\u9700\u5f53\u9762\u6c9f\u901a\uff0c\u60a8\u53ef\u5728\u6bcf\u5468\u4e00\u7684\u6cd5\u5b98\u63a5\u5f85\u65e5\u524d\u5f80\u4e0b\u57ce\u533a\u6cd5\u9662\u4e0e\u6267\u884c\u6cd5\u5b98\u9762\u5bf9\u9762\u54a8\u8be2\uff0c\u8bf7\u95ee\u8fd8\u6709\u4ec0\u4e48\u9700\u8981\u5e2e\u60a8\uff0c&", "vc_robot_complain": "", "vc_robot_court": "", "vc_robot_judge": "", "vc_robot_lawsuit": "", "vc_robot_welcome": "\u5f88\u62b1\u6b49\uff0c\u6211\u6ca1\u6709\u542c\u61c2\u60a8\u7684\u610f\u601d\uff0c\u60a8\u53ef\u4ee5\u8fdb\u884c\u6848\u4ef6\u67e5\u8be2\u3001\u8054\u7cfb\u6cd5\u5b98\uff0c\u8bf7\u95ee\u60a8\u9700\u8981\u4ec0\u4e48\u5e2e\u52a9\uff1f&\u8bf7\u6309\u952e\u8f93\u5165\u5f53\u4e8b\u4eba\u7684\u8eab\u4efd\u8bc1\u53f7\uff0c\u5b57\u6bcd\u7528*\u53f7\u952e\u4ee3\u66ff\uff0c\u6309#\u53f7\u952e\u7ed3\u675f\uff0c\u8fd4\u56de\u4e3b\u83dc\u5355\u8bf7\u76f4\u63a5\u6309#\u53f7\u952e\uff0c\u60a8\u4e5f\u53ef\u4ee5\u767b\u5f55\u6d59\u6c5f\u79fb\u52a8\u5fae\u6cd5\u9662\u6216\u6d59\u6c5f\u6cd5\u9662\u7f51\u8fdb\u884c\u7ebf\u4e0a\u4e00\u5bf9\u4e00\u54a8\u8be2\uff0c&", "vc_user_case": "362326197909193939&2019&11\u6708&2018\u5e741\u6708&\u55ef\uff0c\u5bf9\u662f\u7684&\u67e5\u4e00\u4e0b\u5f00\u5ead\u65f6\u95f4&", "vc_user_complain": "", "vc_user_court": "", "vc_user_judge": "", "vc_user_lawsuit": "", "vc_user_welcome": "\u55ef&\u6848\u4ef6\u67e5\u8be2&"}

print(type(d))
print(type(json.dumps(d)))
r = requests.post(url, json=json.dumps(d))
print(r.status_code)