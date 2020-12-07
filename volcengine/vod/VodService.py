# coding:utf-8

from __future__ import print_function

import threading
from zlib import crc32

from volcengine.ApiInfo import ApiInfo
from volcengine.Credentials import Credentials
from volcengine.ServiceInfo import ServiceInfo
from volcengine.base.Service import Service


class VodService(Service):

    def __init__(self, region='cn-north-1'):
        self.service_info = VodService.get_service_info(region)
        self.api_info = VodService.get_api_info()
        self.domain_cache = {}
        self.fallback_domain_weights = {}
        self.update_interval = 10
        self.lock = threading.Lock()
        super(VodService, self).__init__(self.service_info, self.api_info)

    # TODO 测试完毕修改回来
    @staticmethod
    def get_service_info(region):
        service_info_map = {
            # 'cn-north-1': ServiceInfo("vod.volcengineapi.com", {'Accept': 'application/json'},
            #                           Credentials('', '', 'vod', 'cn-north-1'), 5, 5),
            'cn-north-1': ServiceInfo("volcengineapi-boe.byted.org", {'Accept': 'application/json'},
                                      Credentials('', '', 'vod', 'cn-north-1'), 5, 5),
            'ap-singapore-1': ServiceInfo("vod.ap-singapore-1.volcengineapi.com", {'Accept': 'application/json'},
                                          Credentials('', '', 'vod', 'ap-singapore-1'), 5, 5),
            'us-east-1': ServiceInfo("vod.us-east-1.volcengineapi.com", {'Accept': 'application/json'},
                                     Credentials('', '', 'vod', 'us-east-1'), 5, 5),
        }
        service_info = service_info_map.get(region, None)
        if not service_info:
            raise Exception('Cant find the region, please check it carefully')

        return service_info

    @staticmethod
    def get_api_info():
        api_info = {
            "GetPlayInfo": ApiInfo("GET", "/", {"Action": "GetPlayInfo", "Version": "2020-08-01"}, {}, {}),
            "GetOriginalPlayInfo": ApiInfo("GET", "/", {"Action": "GetOriginalPlayInfo", "Version": "2020-08-01"}, {},
                                           {}),
            "StartWorkflow": ApiInfo("GET", "/", {"Action": "StartWorkflow", "Version": "2020-08-01"}, {}, {}),
            "UpdateMediaPublishStatus": ApiInfo("GET", "/",
                                                {"Action": "UpdateMediaPublishStatus", "Version": "2020-08-01"},
                                                {}, {}),
            "UpdateMediaInfo": ApiInfo("GET", "/", {"Action": "UpdateMediaInfo", "Version": "2020-08-01"}, {}, {}),
            "GetMediaInfos": ApiInfo("GET", "/", {"Action": "GetMediaInfos", "Version": "2020-08-01"}, {}, {}),
            "GetRecommendedPoster": ApiInfo("GET", "/", {"Action": "GetRecommendedPoster", "Version": "2020-08-01"}, {},
                                            {}),
            "UploadMediaByUrl": ApiInfo("GET", "/", {"Action": "UploadVideoByUrl", "Version": "2020-08-01"}, {}, {}),
            "QueryUploadTaskInfo": ApiInfo("GET", "/", {"Action": "QueryUploadTaskInfo", "Version": "2020-08-01"}, {},
                                           {}),
            "ApplyUploadInfo": ApiInfo("GET", "/", {"Action": "ApplyUploadInfo", "Version": "2020-08-01"}, {}, {}),
            "CommitUploadInfo": ApiInfo("GET", "/", {"Action": "CommitUploadInfo", "Version": "2020-08-01"}, {}, {}),
        }
        return api_info

    @staticmethod
    def crc32(file_path):
        prev = 0
        for eachLine in open(file_path, "rb"):
            prev = crc32(eachLine, prev)
        return prev & 0xFFFFFFFF
