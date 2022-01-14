#  -*- coding: utf-8 -*-
from volcengine.example.cdn import ak, sk
from volcengine.cdn.service import CDNService

if __name__ == '__main__':
    svc = CDNService()
    svc.set_ak(ak)
    svc.set_sk(sk)

    body = {
        "Urls": "http://example.com/1.txt\nhttp://example.com/2.jpg",
    }

    resp = svc.submit_preload_task(body)
    print(resp)