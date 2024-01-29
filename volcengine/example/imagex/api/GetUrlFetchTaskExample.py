# coding:utf-8
from volcengine.imagex.imagex_service import ImagexService

if __name__ == '__main__':
    service = ImagexService()

    # call below method if you dont set ak and sk in $HOME/.volc/config
    service.set_ak('ak')
    service.set_sk('sk')

    query = {}

    resp = service.get_url_fetch_task(query)
    print(resp)
