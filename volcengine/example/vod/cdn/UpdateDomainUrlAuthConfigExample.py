# coding:utf-8
from __future__ import print_function

from volcengine.vod.VodService import VodService
from volcengine.vod.models.request.request_vod_pb2 import VodUpdateDomainUrlAuthConfigV2Request

if __name__ == '__main__':
    vod_service = VodService()
    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    vod_service.set_ak('your ak')
    vod_service.set_sk('your sk')
    try:
        req = VodUpdateDomainUrlAuthConfigV2Request()
        req.SpaceName = 'your space name'
        req.DomainType= 'your DomainType'
        req.Domain    = 'your Domain'
        req.MainKey   = 'your MainKey'
        req.BackupKey = 'your BackupKey'
        req.Status    = 'your Status'
        resp = vod_service.update_domain_url_auth_config(req)
    except Exception:
        raise
    else:
        print(resp)
        if resp.ResponseMetadata.Error.Code != '':
            print(resp.ResponseMetadata.Error)
