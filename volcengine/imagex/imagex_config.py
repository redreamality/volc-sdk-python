# coding:utf-8

from volcengine.ServiceInfo import ServiceInfo
from volcengine.Credentials import Credentials
from volcengine.ApiInfo import ApiInfo

service_info_map = {
    'cn-north-1': ServiceInfo(
        'imagex.volcengineapi.com',
        {'Accept': 'application/json'},
        Credentials('', '', 'ImageX', 'cn-north-1'),
        10, 10, "https"),
    'ap-singapore-1': ServiceInfo(
        'imagex-ap-singapore-1.volcengineapi.com',
        {'Accept': 'application/json'},
        Credentials('', '', 'ImageX', 'ap-singapore-1'),
        10, 10, "https"),
    'us-east-1': ServiceInfo(
        'imagex-us-east-1.volcengineapi.com',
        {'Accept': 'application/json'},
        Credentials('', '', 'ImageX', 'us-east-1'),
        10, 10, "https")
}

api_info = {
    "DelDomain": ApiInfo("POST", "/", {"Action": "DelDomain", "Version": "2023-05-01"}, {}, {}),
    "UpdateRefer": ApiInfo("POST", "/", {"Action": "UpdateRefer", "Version": "2018-08-01"}, {}, {}),
    "UpdateHttps": ApiInfo("POST", "/", {"Action": "UpdateHttps", "Version": "2018-08-01"}, {}, {}),
    "UpdateResponseHeader": ApiInfo("POST", "/", {"Action": "UpdateResponseHeader", "Version": "2018-08-01"}, {}, {}),
    "SetDefaultDomain": ApiInfo("POST", "/", {"Action": "SetDefaultDomain", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageVolcCdnAccessLog": ApiInfo("POST", "/", {"Action": "DescribeImageVolcCdnAccessLog", "Version": "2018-08-01"}, {}, {}),
    "GetResponseHeaderValidateKeys": ApiInfo("GET", "/", {"Action": "GetResponseHeaderValidateKeys", "Version": "2023-05-01"}, {}, {}),
    "GetDomainConfig": ApiInfo("GET", "/", {"Action": "GetDomainConfig", "Version": "2018-08-01"}, {}, {}),
    "GetServiceDomains": ApiInfo("GET", "/", {"Action": "GetServiceDomains", "Version": "2018-08-01"}, {}, {}),
    "CreateImageMigrateTask": ApiInfo("POST", "/", {"Action": "CreateImageMigrateTask", "Version": "2018-08-01"}, {}, {}),
    "DeleteImageMigrateTask": ApiInfo("POST", "/", {"Action": "DeleteImageMigrateTask", "Version": "2018-08-01"}, {}, {}),
    "ExportFailedMigrateTask": ApiInfo("GET", "/", {"Action": "ExportFailedMigrateTask", "Version": "2018-08-01"}, {}, {}),
    "UpdateImageTaskStrategy": ApiInfo("POST", "/", {"Action": "UpdateImageTaskStrategy", "Version": "2018-08-01"}, {}, {}),
    "TerminateImageMigrateTask": ApiInfo("POST", "/", {"Action": "TerminateImageMigrateTask", "Version": "2018-08-01"}, {}, {}),
    "GetVendorBuckets": ApiInfo("POST", "/", {"Action": "GetVendorBuckets", "Version": "2018-08-01"}, {}, {}),
    "GetImageMigrateTasks": ApiInfo("GET", "/", {"Action": "GetImageMigrateTasks", "Version": "2018-08-01"}, {}, {}),
    "RerunImageMigrateTask": ApiInfo("POST", "/", {"Action": "RerunImageMigrateTask", "Version": "2018-08-01"}, {}, {}),
    "DescribeImageXSummary": ApiInfo("GET", "/", {"Action": "DescribeImageXSummary", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXDomainTrafficData": ApiInfo("GET", "/", {"Action": "DescribeImageXDomainTrafficData", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXDomainBandwidthData": ApiInfo("GET", "/", {"Action": "DescribeImageXDomainBandwidthData", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXDomainBandwidthNinetyFiveData": ApiInfo("GET", "/", {"Action": "DescribeImageXDomainBandwidthNinetyFiveData", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXBucketUsage": ApiInfo("GET", "/", {"Action": "DescribeImageXBucketUsage", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXBillingRequestCntUsage": ApiInfo("GET", "/", {"Action": "DescribeImageXBillingRequestCntUsage", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXRequestCntUsage": ApiInfo("GET", "/", {"Action": "DescribeImageXRequestCntUsage", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXBaseOpUsage": ApiInfo("GET", "/", {"Action": "DescribeImageXBaseOpUsage", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXCompressUsage": ApiInfo("GET", "/", {"Action": "DescribeImageXCompressUsage", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXScreenshotUsage": ApiInfo("GET", "/", {"Action": "DescribeImageXScreenshotUsage", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXVideoClipDurationUsage": ApiInfo("GET", "/", {"Action": "DescribeImageXVideoClipDurationUsage", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXMultiCompressUsage": ApiInfo("GET", "/", {"Action": "DescribeImageXMultiCompressUsage", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXEdgeRequest": ApiInfo("GET", "/", {"Action": "DescribeImageXEdgeRequest", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXEdgeRequestBandwidth": ApiInfo("GET", "/", {"Action": "DescribeImageXEdgeRequestBandwidth", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXEdgeRequestTraffic": ApiInfo("GET", "/", {"Action": "DescribeImageXEdgeRequestTraffic", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXEdgeRequestRegions": ApiInfo("GET", "/", {"Action": "DescribeImageXEdgeRequestRegions", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXMirrorRequestHttpCodeByTime": ApiInfo("POST", "/", {"Action": "DescribeImageXMirrorRequestHttpCodeByTime", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXMirrorRequestHttpCodeOverview": ApiInfo("POST", "/", {"Action": "DescribeImageXMirrorRequestHttpCodeOverview", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXMirrorRequestTraffic": ApiInfo("POST", "/", {"Action": "DescribeImageXMirrorRequestTraffic", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXMirrorRequestBandwidth": ApiInfo("POST", "/", {"Action": "DescribeImageXMirrorRequestBandwidth", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXServerQPSUsage": ApiInfo("GET", "/", {"Action": "DescribeImageXServerQPSUsage", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXHitRateTrafficData": ApiInfo("GET", "/", {"Action": "DescribeImageXHitRateTrafficData", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXHitRateRequestData": ApiInfo("GET", "/", {"Action": "DescribeImageXHitRateRequestData", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXCDNTopRequestData": ApiInfo("GET", "/", {"Action": "DescribeImageXCDNTopRequestData", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXServiceQuality": ApiInfo("GET", "/", {"Action": "DescribeImageXServiceQuality", "Version": "2023-05-01"}, {}, {}),
    "GetImageXQueryApps": ApiInfo("GET", "/", {"Action": "GetImageXQueryApps", "Version": "2023-05-01"}, {}, {}),
    "GetImageXQueryRegions": ApiInfo("GET", "/", {"Action": "GetImageXQueryRegions", "Version": "2023-05-01"}, {}, {}),
    "GetImageXQueryDims": ApiInfo("GET", "/", {"Action": "GetImageXQueryDims", "Version": "2023-05-01"}, {}, {}),
    "GetImageXQueryVals": ApiInfo("GET", "/", {"Action": "GetImageXQueryVals", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXUploadCountByTime": ApiInfo("POST", "/", {"Action": "DescribeImageXUploadCountByTime", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXUploadDuration": ApiInfo("POST", "/", {"Action": "DescribeImageXUploadDuration", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXUploadSuccessRateByTime": ApiInfo("POST", "/", {"Action": "DescribeImageXUploadSuccessRateByTime", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXUploadFileSize": ApiInfo("POST", "/", {"Action": "DescribeImageXUploadFileSize", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXUploadErrorCodeByTime": ApiInfo("POST", "/", {"Action": "DescribeImageXUploadErrorCodeByTime", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXUploadErrorCodeAll": ApiInfo("POST", "/", {"Action": "DescribeImageXUploadErrorCodeAll", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXUploadSpeed": ApiInfo("POST", "/", {"Action": "DescribeImageXUploadSpeed", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXUploadSegmentSpeedByTime": ApiInfo("POST", "/", {"Action": "DescribeImageXUploadSegmentSpeedByTime", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXCdnSuccessRateByTime": ApiInfo("POST", "/", {"Action": "DescribeImageXCdnSuccessRateByTime", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXCdnSuccessRateAll": ApiInfo("POST", "/", {"Action": "DescribeImageXCdnSuccessRateAll", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXCdnErrorCodeByTime": ApiInfo("POST", "/", {"Action": "DescribeImageXCdnErrorCodeByTime", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXCdnErrorCodeAll": ApiInfo("POST", "/", {"Action": "DescribeImageXCdnErrorCodeAll", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXCdnDurationDetailByTime": ApiInfo("POST", "/", {"Action": "DescribeImageXCdnDurationDetailByTime", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXCdnDurationAll": ApiInfo("POST", "/", {"Action": "DescribeImageXCdnDurationAll", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXCdnReuseRateByTime": ApiInfo("POST", "/", {"Action": "DescribeImageXCdnReuseRateByTime", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXCdnReuseRateAll": ApiInfo("POST", "/", {"Action": "DescribeImageXCdnReuseRateAll", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXCdnProtocolRateByTime": ApiInfo("POST", "/", {"Action": "DescribeImageXCdnProtocolRateByTime", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXClientFailureRate": ApiInfo("POST", "/", {"Action": "DescribeImageXClientFailureRate", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXClientDecodeSuccessRateByTime": ApiInfo("POST", "/", {"Action": "DescribeImageXClientDecodeSuccessRateByTime", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXClientDecodeDurationByTime": ApiInfo("POST", "/", {"Action": "DescribeImageXClientDecodeDurationByTime", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXClientQueueDurationByTime": ApiInfo("POST", "/", {"Action": "DescribeImageXClientQueueDurationByTime", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXClientErrorCodeByTime": ApiInfo("POST", "/", {"Action": "DescribeImageXClientErrorCodeByTime", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXClientErrorCodeAll": ApiInfo("POST", "/", {"Action": "DescribeImageXClientErrorCodeAll", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXClientLoadDuration": ApiInfo("POST", "/", {"Action": "DescribeImageXClientLoadDuration", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXClientLoadDurationAll": ApiInfo("POST", "/", {"Action": "DescribeImageXClientLoadDurationAll", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXClientSdkVerByTime": ApiInfo("POST", "/", {"Action": "DescribeImageXClientSdkVerByTime", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXClientFileSize": ApiInfo("POST", "/", {"Action": "DescribeImageXClientFileSize", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXClientTopFileSize": ApiInfo("POST", "/", {"Action": "DescribeImageXClientTopFileSize", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXClientCountByTime": ApiInfo("POST", "/", {"Action": "DescribeImageXClientCountByTime", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXClientQualityRateByTime": ApiInfo("POST", "/", {"Action": "DescribeImageXClientQualityRateByTime", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXClientTopQualityURL": ApiInfo("POST", "/", {"Action": "DescribeImageXClientTopQualityURL", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXClientDemotionRateByTime": ApiInfo("POST", "/", {"Action": "DescribeImageXClientDemotionRateByTime", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXClientTopDemotionURL": ApiInfo("POST", "/", {"Action": "DescribeImageXClientTopDemotionURL", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXClientScoreByTime": ApiInfo("POST", "/", {"Action": "DescribeImageXClientScoreByTime", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXSensibleCountByTime": ApiInfo("POST", "/", {"Action": "DescribeImageXSensibleCountByTime", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXSensibleCacheHitRateByTime": ApiInfo("POST", "/", {"Action": "DescribeImageXSensibleCacheHitRateByTime", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXSensibleTopSizeURL": ApiInfo("POST", "/", {"Action": "DescribeImageXSensibleTopSizeURL", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXSensibleTopResolutionURL": ApiInfo("POST", "/", {"Action": "DescribeImageXSensibleTopResolutionURL", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXSensibleTopRamURL": ApiInfo("POST", "/", {"Action": "DescribeImageXSensibleTopRamURL", "Version": "2023-05-01"}, {}, {}),
    "DescribeImageXSensibleTopUnknownURL": ApiInfo("POST", "/", {"Action": "DescribeImageXSensibleTopUnknownURL", "Version": "2023-05-01"}, {}, {}),
    "GetImageStorageFiles": ApiInfo("GET", "/", {"Action": "GetImageStorageFiles", "Version": "2018-08-01"}, {}, {}),
    "DeleteImageUploadFiles": ApiInfo("POST", "/", {"Action": "DeleteImageUploadFiles", "Version": "2018-08-01"}, {}, {}),
    "UpdateImageUploadFiles": ApiInfo("POST", "/", {"Action": "UpdateImageUploadFiles", "Version": "2023-05-01"}, {}, {}),
    "CommitImageUpload": ApiInfo("POST", "/", {"Action": "CommitImageUpload", "Version": "2018-08-01"}, {}, {}),
    "ApplyImageUpload": ApiInfo("GET", "/", {"Action": "ApplyImageUpload", "Version": "2018-08-01"}, {}, {}),
    "GetImageUploadFile": ApiInfo("GET", "/", {"Action": "GetImageUploadFile", "Version": "2023-05-01"}, {}, {}),
    "GetImageUploadFiles": ApiInfo("GET", "/", {"Action": "GetImageUploadFiles", "Version": "2018-08-01"}, {}, {}),
    "GetImageUpdateFiles": ApiInfo("GET", "/", {"Action": "GetImageUpdateFiles", "Version": "2023-05-01"}, {}, {}),
    "PreviewImageUploadFile": ApiInfo("GET", "/", {"Action": "PreviewImageUploadFile", "Version": "2023-05-01"}, {}, {}),
    "GetImageService": ApiInfo("GET", "/", {"Action": "GetImageService", "Version": "2018-08-01"}, {}, {}),
    "GetAllImageServices": ApiInfo("GET", "/", {"Action": "GetAllImageServices", "Version": "2018-08-01"}, {}, {}),
    "CreateImageCompressTask": ApiInfo("POST", "/", {"Action": "CreateImageCompressTask", "Version": "2018-08-01"}, {}, {}),
    "FetchImageUrl": ApiInfo("POST", "/", {"Action": "FetchImageUrl", "Version": "2023-05-01"}, {}, {}),
    "UpdateImageStorageTTL": ApiInfo("POST", "/", {"Action": "UpdateImageStorageTTL", "Version": "2023-05-01"}, {}, {}),
    "GetCompressTaskInfo": ApiInfo("GET", "/", {"Action": "GetCompressTaskInfo", "Version": "2018-08-01"}, {}, {}),
    "GetUrlFetchTask": ApiInfo("GET", "/", {"Action": "GetUrlFetchTask", "Version": "2018-08-01"}, {}, {}),
    "GetResourceURL": ApiInfo("GET", "/", {"Action": "GetResourceURL", "Version": "2023-05-01"}, {}, {}),
    "UpdateImageFileKey": ApiInfo("POST", "/", {"Action": "UpdateImageFileKey", "Version": "2018-08-01"}, {}, {}),
    "CreateImageContentTask": ApiInfo("POST", "/", {"Action": "CreateImageContentTask", "Version": "2023-05-01"}, {}, {}),
    "GetImageContentTaskDetail": ApiInfo("POST", "/", {"Action": "GetImageContentTaskDetail", "Version": "2023-05-01"}, {}, {}),
    "GetImageContentBlockList": ApiInfo("POST", "/", {"Action": "GetImageContentBlockList", "Version": "2023-05-01"}, {}, {}),
    "CreateImageTranscodeQueue": ApiInfo("POST", "/", {"Action": "CreateImageTranscodeQueue", "Version": "2023-05-01"}, {}, {}),
    "DeleteImageTranscodeQueue": ApiInfo("POST", "/", {"Action": "DeleteImageTranscodeQueue", "Version": "2023-05-01"}, {}, {}),
    "UpdateImageTranscodeQueue": ApiInfo("POST", "/", {"Action": "UpdateImageTranscodeQueue", "Version": "2023-05-01"}, {}, {}),
    "UpdateImageTranscodeQueueStatus": ApiInfo("POST", "/", {"Action": "UpdateImageTranscodeQueueStatus", "Version": "2023-05-01"}, {}, {}),
    "GetImageTranscodeQueues": ApiInfo("GET", "/", {"Action": "GetImageTranscodeQueues", "Version": "2023-05-01"}, {}, {}),
    "CreateImageTranscodeTask": ApiInfo("POST", "/", {"Action": "CreateImageTranscodeTask", "Version": "2023-05-01"}, {}, {}),
    "GetImageTranscodeDetails": ApiInfo("GET", "/", {"Action": "GetImageTranscodeDetails", "Version": "2023-05-01"}, {}, {}),
    "CreateImageTranscodeCallback": ApiInfo("POST", "/", {"Action": "CreateImageTranscodeCallback", "Version": "2023-05-01"}, {}, {}),
    "DeleteImageTranscodeDetail": ApiInfo("POST", "/", {"Action": "DeleteImageTranscodeDetail", "Version": "2023-05-01"}, {}, {}),
    "GetImagePSDetection": ApiInfo("POST", "/", {"Action": "GetImagePSDetection", "Version": "2023-05-01"}, {}, {}),
    "GetImageEraseResult": ApiInfo("POST", "/", {"Action": "GetImageEraseResult", "Version": "2023-05-01"}, {}, {}),
    "GetImageSuperResolutionResult": ApiInfo("POST", "/", {"Action": "GetImageSuperResolutionResult", "Version": "2023-05-01"}, {}, {}),
    "GetImageDuplicateDetection": ApiInfo("POST", "/", {"Action": "GetImageDuplicateDetection", "Version": "2018-08-01"}, {}, {}),
    "GetImageOCRV2": ApiInfo("POST", "/", {"Action": "GetImageOCRV2", "Version": "2018-08-01"}, {}, {}),
    "GetImageBgFillResult": ApiInfo("POST", "/", {"Action": "GetImageBgFillResult", "Version": "2023-05-01"}, {}, {}),
    "GetSegmentImage": ApiInfo("POST", "/", {"Action": "GetSegmentImage", "Version": "2023-05-01"}, {}, {}),
    "GetImageSmartCropResult": ApiInfo("POST", "/", {"Action": "GetImageSmartCropResult", "Version": "2023-05-01"}, {}, {}),
    "GetImageComicResult": ApiInfo("POST", "/", {"Action": "GetImageComicResult", "Version": "2023-05-01"}, {}, {}),
    "GetImageEnhanceResult": ApiInfo("POST", "/", {"Action": "GetImageEnhanceResult", "Version": "2018-08-01"}, {}, {}),
    "GetImageQuality": ApiInfo("POST", "/", {"Action": "GetImageQuality", "Version": "2018-08-01"}, {}, {}),
    "GetPrivateImageType": ApiInfo("POST", "/", {"Action": "GetPrivateImageType", "Version": "2018-08-01"}, {}, {}),
    "CreateHiddenWatermarkImage": ApiInfo("POST", "/", {"Action": "CreateHiddenWatermarkImage", "Version": "2023-05-01"}, {}, {}),
    "CreateImageHmExtract": ApiInfo("POST", "/", {"Action": "CreateImageHmExtract", "Version": "2023-05-01"}, {}, {}),
    "CreateImageHmEmbed": ApiInfo("POST", "/", {"Action": "CreateImageHmEmbed", "Version": "2023-05-01"}, {}, {}),
    "GetComprehensiveEnhanceImage": ApiInfo("POST", "/", {"Action": "GetComprehensiveEnhanceImage", "Version": "2023-05-01"}, {}, {}),
    "GetImageEraseModels": ApiInfo("GET", "/", {"Action": "GetImageEraseModels", "Version": "2023-05-01"}, {}, {}),
    "GetDedupTaskStatus": ApiInfo("GET", "/", {"Action": "GetDedupTaskStatus", "Version": "2018-08-01"}, {}, {}),
    "CreateImageService": ApiInfo("POST", "/", {"Action": "CreateImageService", "Version": "2023-05-01"}, {}, {}),
    "DeleteImageService": ApiInfo("POST", "/", {"Action": "DeleteImageService", "Version": "2023-05-01"}, {}, {}),
    "UpdateImageAuthKey": ApiInfo("POST", "/", {"Action": "UpdateImageAuthKey", "Version": "2023-05-01"}, {}, {}),
    "UpdateServiceName": ApiInfo("POST", "/", {"Action": "UpdateServiceName", "Version": "2023-05-01"}, {}, {}),
    "UpdateImageObjectAccess": ApiInfo("POST", "/", {"Action": "UpdateImageObjectAccess", "Version": "2023-05-01"}, {}, {}),
    "UpdateImageMirrorConf": ApiInfo("POST", "/", {"Action": "UpdateImageMirrorConf", "Version": "2018-08-01"}, {}, {}),
    "GetImageServiceSubscription": ApiInfo("GET", "/", {"Action": "GetImageServiceSubscription", "Version": "2023-05-01"}, {}, {}),
    "GetImageAuthKey": ApiInfo("GET", "/", {"Action": "GetImageAuthKey", "Version": "2023-05-01"}, {}, {}),
    "CreateImageAnalyzeTask": ApiInfo("POST", "/", {"Action": "CreateImageAnalyzeTask", "Version": "2023-05-01"}, {}, {}),
    "DeleteImageAnalyzeTaskRun": ApiInfo("POST", "/", {"Action": "DeleteImageAnalyzeTaskRun", "Version": "2023-05-01"}, {}, {}),
    "DeleteImageAnalyzeTask": ApiInfo("POST", "/", {"Action": "DeleteImageAnalyzeTask", "Version": "2023-05-01"}, {}, {}),
    "UpdateImageAnalyzeTaskStatus": ApiInfo("POST", "/", {"Action": "UpdateImageAnalyzeTaskStatus", "Version": "2023-05-01"}, {}, {}),
    "UpdateImageAnalyzeTask": ApiInfo("POST", "/", {"Action": "UpdateImageAnalyzeTask", "Version": "2023-05-01"}, {}, {}),
    "GetImageAnalyzeTasks": ApiInfo("GET", "/", {"Action": "GetImageAnalyzeTasks", "Version": "2023-05-01"}, {}, {}),
    "GetImageAnalyzeResult": ApiInfo("GET", "/", {"Action": "GetImageAnalyzeResult", "Version": "2023-05-01"}, {}, {}),
    "GetImageStyleResult": ApiInfo("POST", "/", {"Action": "GetImageStyleResult", "Version": "2018-08-01"}, {}, {}),
    "CreateImageTemplate": ApiInfo("POST", "/", {"Action": "CreateImageTemplate", "Version": "2018-08-01"}, {}, {}),
    "DeleteTemplatesFromBin": ApiInfo("POST", "/", {"Action": "DeleteTemplatesFromBin", "Version": "2023-05-01"}, {}, {}),
    "DeleteImageTemplate": ApiInfo("POST", "/", {"Action": "DeleteImageTemplate", "Version": "2023-05-01"}, {}, {}),
    "CreateTemplatesFromBin": ApiInfo("POST", "/", {"Action": "CreateTemplatesFromBin", "Version": "2023-05-01"}, {}, {}),
    "GetImageTemplate": ApiInfo("GET", "/", {"Action": "GetImageTemplate", "Version": "2018-08-01"}, {}, {}),
    "GetTemplatesFromBin": ApiInfo("GET", "/", {"Action": "GetTemplatesFromBin", "Version": "2018-08-01"}, {}, {}),
    "GetAllImageTemplates": ApiInfo("GET", "/", {"Action": "GetAllImageTemplates", "Version": "2018-08-01"}, {}, {}),
    "CreateImageAuditTask": ApiInfo("POST", "/", {"Action": "CreateImageAuditTask", "Version": "2023-05-01"}, {}, {}),
    "DeleteImageAuditResult": ApiInfo("POST", "/", {"Action": "DeleteImageAuditResult", "Version": "2023-05-01"}, {}, {}),
    "UpdateImageAuditTaskStatus": ApiInfo("POST", "/", {"Action": "UpdateImageAuditTaskStatus", "Version": "2023-05-01"}, {}, {}),
    "UpdateImageAuditTask": ApiInfo("POST", "/", {"Action": "UpdateImageAuditTask", "Version": "2023-05-01"}, {}, {}),
    "UpdateAuditImageStatus": ApiInfo("POST", "/", {"Action": "UpdateAuditImageStatus", "Version": "2023-05-01"}, {}, {}),
    "GetImageAuditTasks": ApiInfo("GET", "/", {"Action": "GetImageAuditTasks", "Version": "2023-05-01"}, {}, {}),
    "GetImageAuditResult": ApiInfo("GET", "/", {"Action": "GetImageAuditResult", "Version": "2023-05-01"}, {}, {}),
    "GetAuditEntrysCount": ApiInfo("GET", "/", {"Action": "GetAuditEntrysCount", "Version": "2023-05-01"}, {}, {}),
    "CreateImageRetryAuditTask": ApiInfo("POST", "/", {"Action": "CreateImageRetryAuditTask", "Version": "2023-05-01"}, {}, {})
}