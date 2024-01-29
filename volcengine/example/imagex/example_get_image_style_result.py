# coding:utf-8
from __future__ import print_function
from volcengine.imagex.imagex_service import ImagexService

if __name__ == "__main__":
    imagex_service = ImagexService()

    # call below method if you dont set ak and sk in $HOME/.volc/config
    imagex_service.set_ak("ak")
    imagex_service.set_sk("sk")

    query = {
        "ServiceId": "service id",
    }
    body = {
        "StyleId": "style id",
        "Params": {
            "key": "value",
        },
        "OutputFormat": "jpeg",
        "OutputQuality": 90,
    }

    resp = imagex_service.get_image_style_result(query, body)
    print(resp)
