# coding:utf-8
from volcengine.imagex.imagex_service import ImagexService

if __name__ == '__main__':
    service = ImagexService()

    # call below method if you dont set ak and sk in $HOME/.volc/config
    service.set_ak('ak')
    service.set_sk('sk')

    body = {}

    resp = service.describe_imagex_mirror_request_http_code_overview(body)
    print(resp)
