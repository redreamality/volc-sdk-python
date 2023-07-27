# coding:utf-8
from __future__ import print_function

import json

from volcengine.billing.BillingService import BillingService

if __name__ == '__main__':
    testAk = "<Your AK>"
    testSk = "<Your SK>"

    billing_service = BillingService()
    billing_service.set_ak(testAk)
    billing_service.set_sk(testSk)

    params = dict()
    params['BillPeriod'] = ''
    params['AmortizedMonth'] = '2023-06'
    params['AmortizedDay'] = ''
    params['Product'] = ''
    params['InstanceNo'] = ''
    params['BillingMode'] = ''
    params['BillCategory'] = ''
    params['AmortizedType'] = ''
    params['IgnoreZero'] = 0
    params['NeedRecordNum'] = 0
    params['Offset'] = 0
    params['Limit'] = 10

    body = {}

    resp = billing_service.list_amortized_cost_bill_detail(params, body)
    print(json.dumps(resp, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':')))
