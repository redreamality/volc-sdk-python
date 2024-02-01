# coding:utf-8
from __future__ import print_function

from volcengine.bioos.BioOsService import BioOsService


if __name__ == '__main__':
    # set endpoint/region here if the default value is unsatisfied
    bioos_service = BioOsService(endpoint='endpoint', region='region')

    # call below method if you don't set ak and sk in $HOME/.volc/config
    bioos_service.set_ak('ak')
    bioos_service.set_sk('sk')

    params = {
        'BaseImage': 'base_image',
        'ImageName': 'image_name',
        'DisplayName': 'custom',
        'Source': 'building',
        'Packages': {
            'Pip': {'numpy': '1.22.2'},
        },
        'ImageVersion': '1.0.0',
    }

    resp = bioos_service.create_notebook_server_image(params)
    print(resp)