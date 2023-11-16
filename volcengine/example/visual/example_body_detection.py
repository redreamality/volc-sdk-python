# coding:utf-8
from __future__ import print_function

from volcengine.visual.VisualService import VisualService

if __name__ == '__main__':
    visual_service = VisualService()

    # call below method if you don't set ak and sk in $HOME/.volc/config
    visual_service.set_ak('ak')
    visual_service.set_sk('sk')

    form = {
        "req_key":"face_body_detection",
        "max_obj_num":100,
        "binary_data_base64":[""]
    }

    resp = visual_service.body_detection(form)
    print(resp)
