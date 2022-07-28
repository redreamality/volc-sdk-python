# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vod/business/vod_cdn.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from volcengine.vod.models.business import vod_common_pb2 as vod_dot_business_dot_vod__common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1avod/business/vod_cdn.proto\x12\x1eVolcengine.Vod.Models.Business\x1a\x1dvod/business/vod_common.proto\"\xcd\x01\n\x13VodDomainConfigInfo\x12\x11\n\tSpaceName\x18\x01 \x01(\t\x12P\n\x10PlayInstanceInfo\x18\x02 \x01(\x0b\x32\x36.Volcengine.Vod.Models.Business.VodDomainInstanceInfos\x12Q\n\x11ImageInstanceInfo\x18\x03 \x01(\x0b\x32\x36.Volcengine.Vod.Models.Business.VodDomainInstanceInfos\"\xb5\x01\n\x16VodDomainInstanceInfos\x12L\n\rByteInstances\x18\x01 \x03(\x0b\x32\x35.Volcengine.Vod.Models.Business.VodDomainInstanceInfo\x12M\n\x0eOtherInstances\x18\x02 \x03(\x0b\x32\x35.Volcengine.Vod.Models.Business.VodDomainInstanceInfo\"\x9a\x01\n\x15VodDomainInstanceInfo\x12\x12\n\nInstanceId\x18\x01 \x01(\t\x12?\n\x07\x44omains\x18\x02 \x03(\x0b\x32..Volcengine.Vod.Models.Business.VodDomainoInfo\x12\x16\n\x0e\x43\x61nSelfEditing\x18\x03 \x01(\x08\x12\x14\n\x0c\x43onfigStatus\x18\x04 \x01(\t\"\xf1\x01\n\x0eVodDomainoInfo\x12\x0e\n\x06\x44omain\x18\x01 \x01(\t\x12\r\n\x05\x43name\x18\x02 \x01(\t\x12\x14\n\x0c\x43onfigStatus\x18\x03 \x01(\t\x12\x13\n\x0b\x43nameStatus\x18\x04 \x01(\t\x12\x0e\n\x06Status\x18\x05 \x01(\t\x12M\n\x0b\x43\x65rtificate\x18\x06 \x01(\x0b\x32\x38.Volcengine.Vod.Models.Business.VodDomainCertificateInfo\x12\x12\n\nCreateTime\x18\x07 \x01(\t\x12\x12\n\nUpdateTime\x18\x08 \x01(\t\x12\x0e\n\x06Region\x18\t \x01(\t\"\x8f\x01\n\x18VodDomainCertificateInfo\x12\x15\n\rCertificateId\x18\x01 \x01(\t\x12\x17\n\x0f\x43\x65rtificateName\x18\x02 \x01(\t\x12\x16\n\x0e\x43\x65rtificatePub\x18\x03 \x01(\t\x12\x16\n\x0e\x43\x65rtificatePri\x18\x04 \x01(\t\x12\x13\n\x0bHttpsStatus\x18\x05 \x01(\t\"(\n\x16VodCreateCdnTaskResult\x12\x0e\n\x06TaskId\x18\x01 \x01(\t\"x\n\x0eVodContentInfo\x12\x0e\n\x06ItemId\x18\x01 \x01(\t\x12\x0b\n\x03Url\x18\x02 \x01(\t\x12\x0e\n\x06Status\x18\x03 \x01(\t\x12\x10\n\x08TaskType\x18\x04 \x01(\t\x12\x17\n\x0f\x43reateTimestamp\x18\x05 \x01(\x05\x12\x0e\n\x06TaskId\x18\x06 \x01(\t\"\x8f\x01\n\x10VodCdnTaskResult\x12\x12\n\nTotalCount\x18\x01 \x01(\x05\x12\x0f\n\x07PageNum\x18\x02 \x01(\x05\x12\x10\n\x08PageSize\x18\x03 \x01(\x05\x12\x44\n\x0c\x43ontentInfos\x18\x04 \x03(\x0b\x32..Volcengine.Vod.Models.Business.VodContentInfo\"\x7f\n\x16VodCdnAccessLogElement\x12\x13\n\x0b\x44ownloadUrl\x18\x01 \x01(\t\x12\x10\n\x08\x46ileSize\x18\x02 \x01(\x03\x12\x10\n\x08\x46ileName\x18\x03 \x01(\t\x12\x16\n\x0eStartTimestamp\x18\x04 \x01(\x05\x12\x14\n\x0c\x45ndTimestamp\x18\x05 \x01(\x05\"n\n\x13VodCdnAccessLogInfo\x12\x0e\n\x06\x44omain\x18\x01 \x01(\t\x12G\n\x07LogList\x18\x02 \x03(\x0b\x32\x36.Volcengine.Vod.Models.Business.VodCdnAccessLogElement\"^\n\x19VodListCdnAccessLogResult\x12\x41\n\x04Logs\x18\x01 \x03(\x0b\x32\x33.Volcengine.Vod.Models.Business.VodCdnAccessLogInfo\"B\n\x19VodCdnTopAccessUrlElement\x12\x0b\n\x03Url\x18\x01 \x01(\t\x12\n\n\x02Pv\x18\x02 \x01(\x03\x12\x0c\n\x04\x46lux\x18\x03 \x01(\x03\"k\n\x1cVodListCdnTopAccessUrlResult\x12K\n\x08UrlInfos\x18\x01 \x03(\x0b\x32\x39.Volcengine.Vod.Models.Business.VodCdnTopAccessUrlElement\"3\n\x10VodBandwidthData\x12\x0c\n\x04Time\x18\x01 \x01(\t\x12\x11\n\tBandwidth\x18\x02 \x01(\x01\"\x8c\x02\n\'VodDescribeVodDomainBandwidthDataResult\x12\x12\n\nDomainList\x18\x01 \x03(\t\x12\x11\n\tStartTime\x18\x02 \x01(\t\x12\x0f\n\x07\x45ndTime\x18\x03 \x01(\t\x12\x13\n\x0b\x41ggregation\x18\x04 \x01(\x05\x12\x15\n\rBandwidthType\x18\x05 \x01(\t\x12\x15\n\rPeakBandwidth\x18\x06 \x01(\x01\x12\x19\n\x11PeakBandwidthTime\x18\x07 \x01(\t\x12K\n\x11\x42\x61ndwidthDataList\x18\x08 \x03(\x0b\x32\x30.Volcengine.Vod.Models.Business.VodBandwidthData\"\x80\x01\n\x14VodCdnStatisticsData\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\x0e\n\x06Metric\x18\x02 \x01(\t\x12\x10\n\x08\x44\x61taType\x18\x03 \x01(\t\x12\x38\n\x06Points\x18\x04 \x03(\x0b\x32(.Volcengine.Vod.Models.Business.VodPoint\"\x80\x01\n\x1cVodCdnStatisticsCommonResult\x12\x43\n\x05\x44\x61tas\x18\x01 \x03(\x0b\x32\x34.Volcengine.Vod.Models.Business.VodCdnStatisticsData\x12\x1b\n\x13NoPermissionDomains\x18\x02 \x03(\t\"H\n\x0cVodCdnIpInfo\x12\n\n\x02Ip\x18\x01 \x01(\t\x12\r\n\x05\x43\x64nIp\x18\x02 \x01(\x08\x12\x10\n\x08Location\x18\x03 \x01(\t\x12\x0b\n\x03Isp\x18\x04 \x01(\t\"V\n\x17VodDescribeIpInfoResult\x12;\n\x05Infos\x18\x01 \x03(\x0b\x32,.Volcengine.Vod.Models.Business.VodCdnIpInfo\"/\n\x0eVodTrafficData\x12\x0c\n\x04Time\x18\x01 \x01(\t\x12\x0f\n\x07Traffic\x18\x02 \x01(\x01\"\xe8\x01\n%VodDescribeVodDomainTrafficDataResult\x12\x12\n\nDomainList\x18\x01 \x03(\t\x12\x11\n\tStartTime\x18\x02 \x01(\t\x12\x0f\n\x07\x45ndTime\x18\x03 \x01(\t\x12\x13\n\x0b\x41ggregation\x18\x04 \x01(\x05\x12\x13\n\x0bTrafficType\x18\x05 \x01(\t\x12\x14\n\x0cTotalTraffic\x18\x06 \x01(\x01\x12G\n\x0fTrafficDataList\x18\x07 \x03(\x0b\x32..Volcengine.Vod.Models.Business.VodTrafficDataB\xca\x01\n)com.volcengine.service.vod.model.businessB\x06VodCdnP\x01ZAgithub.com/volcengine/volc-sdk-golang/service/vod/models/business\xa0\x01\x01\xd8\x01\x01\xc2\x02\x00\xca\x02 Volc\\Service\\Vod\\Models\\Business\xe2\x02#Volc\\Service\\Vod\\Models\\GPBMetadatab\x06proto3')



_VODDOMAINCONFIGINFO = DESCRIPTOR.message_types_by_name['VodDomainConfigInfo']
_VODDOMAININSTANCEINFOS = DESCRIPTOR.message_types_by_name['VodDomainInstanceInfos']
_VODDOMAININSTANCEINFO = DESCRIPTOR.message_types_by_name['VodDomainInstanceInfo']
_VODDOMAINOINFO = DESCRIPTOR.message_types_by_name['VodDomainoInfo']
_VODDOMAINCERTIFICATEINFO = DESCRIPTOR.message_types_by_name['VodDomainCertificateInfo']
_VODCREATECDNTASKRESULT = DESCRIPTOR.message_types_by_name['VodCreateCdnTaskResult']
_VODCONTENTINFO = DESCRIPTOR.message_types_by_name['VodContentInfo']
_VODCDNTASKRESULT = DESCRIPTOR.message_types_by_name['VodCdnTaskResult']
_VODCDNACCESSLOGELEMENT = DESCRIPTOR.message_types_by_name['VodCdnAccessLogElement']
_VODCDNACCESSLOGINFO = DESCRIPTOR.message_types_by_name['VodCdnAccessLogInfo']
_VODLISTCDNACCESSLOGRESULT = DESCRIPTOR.message_types_by_name['VodListCdnAccessLogResult']
_VODCDNTOPACCESSURLELEMENT = DESCRIPTOR.message_types_by_name['VodCdnTopAccessUrlElement']
_VODLISTCDNTOPACCESSURLRESULT = DESCRIPTOR.message_types_by_name['VodListCdnTopAccessUrlResult']
_VODBANDWIDTHDATA = DESCRIPTOR.message_types_by_name['VodBandwidthData']
_VODDESCRIBEVODDOMAINBANDWIDTHDATARESULT = DESCRIPTOR.message_types_by_name['VodDescribeVodDomainBandwidthDataResult']
_VODCDNSTATISTICSDATA = DESCRIPTOR.message_types_by_name['VodCdnStatisticsData']
_VODCDNSTATISTICSCOMMONRESULT = DESCRIPTOR.message_types_by_name['VodCdnStatisticsCommonResult']
_VODCDNIPINFO = DESCRIPTOR.message_types_by_name['VodCdnIpInfo']
_VODDESCRIBEIPINFORESULT = DESCRIPTOR.message_types_by_name['VodDescribeIpInfoResult']
_VODTRAFFICDATA = DESCRIPTOR.message_types_by_name['VodTrafficData']
_VODDESCRIBEVODDOMAINTRAFFICDATARESULT = DESCRIPTOR.message_types_by_name['VodDescribeVodDomainTrafficDataResult']
VodDomainConfigInfo = _reflection.GeneratedProtocolMessageType('VodDomainConfigInfo', (_message.Message,), {
  'DESCRIPTOR' : _VODDOMAINCONFIGINFO,
  '__module__' : 'vod.business.vod_cdn_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodDomainConfigInfo)
  })
_sym_db.RegisterMessage(VodDomainConfigInfo)

VodDomainInstanceInfos = _reflection.GeneratedProtocolMessageType('VodDomainInstanceInfos', (_message.Message,), {
  'DESCRIPTOR' : _VODDOMAININSTANCEINFOS,
  '__module__' : 'vod.business.vod_cdn_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodDomainInstanceInfos)
  })
_sym_db.RegisterMessage(VodDomainInstanceInfos)

VodDomainInstanceInfo = _reflection.GeneratedProtocolMessageType('VodDomainInstanceInfo', (_message.Message,), {
  'DESCRIPTOR' : _VODDOMAININSTANCEINFO,
  '__module__' : 'vod.business.vod_cdn_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodDomainInstanceInfo)
  })
_sym_db.RegisterMessage(VodDomainInstanceInfo)

VodDomainoInfo = _reflection.GeneratedProtocolMessageType('VodDomainoInfo', (_message.Message,), {
  'DESCRIPTOR' : _VODDOMAINOINFO,
  '__module__' : 'vod.business.vod_cdn_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodDomainoInfo)
  })
_sym_db.RegisterMessage(VodDomainoInfo)

VodDomainCertificateInfo = _reflection.GeneratedProtocolMessageType('VodDomainCertificateInfo', (_message.Message,), {
  'DESCRIPTOR' : _VODDOMAINCERTIFICATEINFO,
  '__module__' : 'vod.business.vod_cdn_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodDomainCertificateInfo)
  })
_sym_db.RegisterMessage(VodDomainCertificateInfo)

VodCreateCdnTaskResult = _reflection.GeneratedProtocolMessageType('VodCreateCdnTaskResult', (_message.Message,), {
  'DESCRIPTOR' : _VODCREATECDNTASKRESULT,
  '__module__' : 'vod.business.vod_cdn_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodCreateCdnTaskResult)
  })
_sym_db.RegisterMessage(VodCreateCdnTaskResult)

VodContentInfo = _reflection.GeneratedProtocolMessageType('VodContentInfo', (_message.Message,), {
  'DESCRIPTOR' : _VODCONTENTINFO,
  '__module__' : 'vod.business.vod_cdn_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodContentInfo)
  })
_sym_db.RegisterMessage(VodContentInfo)

VodCdnTaskResult = _reflection.GeneratedProtocolMessageType('VodCdnTaskResult', (_message.Message,), {
  'DESCRIPTOR' : _VODCDNTASKRESULT,
  '__module__' : 'vod.business.vod_cdn_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodCdnTaskResult)
  })
_sym_db.RegisterMessage(VodCdnTaskResult)

VodCdnAccessLogElement = _reflection.GeneratedProtocolMessageType('VodCdnAccessLogElement', (_message.Message,), {
  'DESCRIPTOR' : _VODCDNACCESSLOGELEMENT,
  '__module__' : 'vod.business.vod_cdn_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodCdnAccessLogElement)
  })
_sym_db.RegisterMessage(VodCdnAccessLogElement)

VodCdnAccessLogInfo = _reflection.GeneratedProtocolMessageType('VodCdnAccessLogInfo', (_message.Message,), {
  'DESCRIPTOR' : _VODCDNACCESSLOGINFO,
  '__module__' : 'vod.business.vod_cdn_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodCdnAccessLogInfo)
  })
_sym_db.RegisterMessage(VodCdnAccessLogInfo)

VodListCdnAccessLogResult = _reflection.GeneratedProtocolMessageType('VodListCdnAccessLogResult', (_message.Message,), {
  'DESCRIPTOR' : _VODLISTCDNACCESSLOGRESULT,
  '__module__' : 'vod.business.vod_cdn_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodListCdnAccessLogResult)
  })
_sym_db.RegisterMessage(VodListCdnAccessLogResult)

VodCdnTopAccessUrlElement = _reflection.GeneratedProtocolMessageType('VodCdnTopAccessUrlElement', (_message.Message,), {
  'DESCRIPTOR' : _VODCDNTOPACCESSURLELEMENT,
  '__module__' : 'vod.business.vod_cdn_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodCdnTopAccessUrlElement)
  })
_sym_db.RegisterMessage(VodCdnTopAccessUrlElement)

VodListCdnTopAccessUrlResult = _reflection.GeneratedProtocolMessageType('VodListCdnTopAccessUrlResult', (_message.Message,), {
  'DESCRIPTOR' : _VODLISTCDNTOPACCESSURLRESULT,
  '__module__' : 'vod.business.vod_cdn_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodListCdnTopAccessUrlResult)
  })
_sym_db.RegisterMessage(VodListCdnTopAccessUrlResult)

VodBandwidthData = _reflection.GeneratedProtocolMessageType('VodBandwidthData', (_message.Message,), {
  'DESCRIPTOR' : _VODBANDWIDTHDATA,
  '__module__' : 'vod.business.vod_cdn_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodBandwidthData)
  })
_sym_db.RegisterMessage(VodBandwidthData)

VodDescribeVodDomainBandwidthDataResult = _reflection.GeneratedProtocolMessageType('VodDescribeVodDomainBandwidthDataResult', (_message.Message,), {
  'DESCRIPTOR' : _VODDESCRIBEVODDOMAINBANDWIDTHDATARESULT,
  '__module__' : 'vod.business.vod_cdn_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodDescribeVodDomainBandwidthDataResult)
  })
_sym_db.RegisterMessage(VodDescribeVodDomainBandwidthDataResult)

VodCdnStatisticsData = _reflection.GeneratedProtocolMessageType('VodCdnStatisticsData', (_message.Message,), {
  'DESCRIPTOR' : _VODCDNSTATISTICSDATA,
  '__module__' : 'vod.business.vod_cdn_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodCdnStatisticsData)
  })
_sym_db.RegisterMessage(VodCdnStatisticsData)

VodCdnStatisticsCommonResult = _reflection.GeneratedProtocolMessageType('VodCdnStatisticsCommonResult', (_message.Message,), {
  'DESCRIPTOR' : _VODCDNSTATISTICSCOMMONRESULT,
  '__module__' : 'vod.business.vod_cdn_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodCdnStatisticsCommonResult)
  })
_sym_db.RegisterMessage(VodCdnStatisticsCommonResult)

VodCdnIpInfo = _reflection.GeneratedProtocolMessageType('VodCdnIpInfo', (_message.Message,), {
  'DESCRIPTOR' : _VODCDNIPINFO,
  '__module__' : 'vod.business.vod_cdn_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodCdnIpInfo)
  })
_sym_db.RegisterMessage(VodCdnIpInfo)

VodDescribeIpInfoResult = _reflection.GeneratedProtocolMessageType('VodDescribeIpInfoResult', (_message.Message,), {
  'DESCRIPTOR' : _VODDESCRIBEIPINFORESULT,
  '__module__' : 'vod.business.vod_cdn_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodDescribeIpInfoResult)
  })
_sym_db.RegisterMessage(VodDescribeIpInfoResult)

VodTrafficData = _reflection.GeneratedProtocolMessageType('VodTrafficData', (_message.Message,), {
  'DESCRIPTOR' : _VODTRAFFICDATA,
  '__module__' : 'vod.business.vod_cdn_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodTrafficData)
  })
_sym_db.RegisterMessage(VodTrafficData)

VodDescribeVodDomainTrafficDataResult = _reflection.GeneratedProtocolMessageType('VodDescribeVodDomainTrafficDataResult', (_message.Message,), {
  'DESCRIPTOR' : _VODDESCRIBEVODDOMAINTRAFFICDATARESULT,
  '__module__' : 'vod.business.vod_cdn_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodDescribeVodDomainTrafficDataResult)
  })
_sym_db.RegisterMessage(VodDescribeVodDomainTrafficDataResult)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n)com.volcengine.service.vod.model.businessB\006VodCdnP\001ZAgithub.com/volcengine/volc-sdk-golang/service/vod/models/business\240\001\001\330\001\001\302\002\000\312\002 Volc\\Service\\Vod\\Models\\Business\342\002#Volc\\Service\\Vod\\Models\\GPBMetadata'
  _VODDOMAINCONFIGINFO._serialized_start=94
  _VODDOMAINCONFIGINFO._serialized_end=299
  _VODDOMAININSTANCEINFOS._serialized_start=302
  _VODDOMAININSTANCEINFOS._serialized_end=483
  _VODDOMAININSTANCEINFO._serialized_start=486
  _VODDOMAININSTANCEINFO._serialized_end=640
  _VODDOMAINOINFO._serialized_start=643
  _VODDOMAINOINFO._serialized_end=884
  _VODDOMAINCERTIFICATEINFO._serialized_start=887
  _VODDOMAINCERTIFICATEINFO._serialized_end=1030
  _VODCREATECDNTASKRESULT._serialized_start=1032
  _VODCREATECDNTASKRESULT._serialized_end=1072
  _VODCONTENTINFO._serialized_start=1074
  _VODCONTENTINFO._serialized_end=1194
  _VODCDNTASKRESULT._serialized_start=1197
  _VODCDNTASKRESULT._serialized_end=1340
  _VODCDNACCESSLOGELEMENT._serialized_start=1342
  _VODCDNACCESSLOGELEMENT._serialized_end=1469
  _VODCDNACCESSLOGINFO._serialized_start=1471
  _VODCDNACCESSLOGINFO._serialized_end=1581
  _VODLISTCDNACCESSLOGRESULT._serialized_start=1583
  _VODLISTCDNACCESSLOGRESULT._serialized_end=1677
  _VODCDNTOPACCESSURLELEMENT._serialized_start=1679
  _VODCDNTOPACCESSURLELEMENT._serialized_end=1745
  _VODLISTCDNTOPACCESSURLRESULT._serialized_start=1747
  _VODLISTCDNTOPACCESSURLRESULT._serialized_end=1854
  _VODBANDWIDTHDATA._serialized_start=1856
  _VODBANDWIDTHDATA._serialized_end=1907
  _VODDESCRIBEVODDOMAINBANDWIDTHDATARESULT._serialized_start=1910
  _VODDESCRIBEVODDOMAINBANDWIDTHDATARESULT._serialized_end=2178
  _VODCDNSTATISTICSDATA._serialized_start=2181
  _VODCDNSTATISTICSDATA._serialized_end=2309
  _VODCDNSTATISTICSCOMMONRESULT._serialized_start=2312
  _VODCDNSTATISTICSCOMMONRESULT._serialized_end=2440
  _VODCDNIPINFO._serialized_start=2442
  _VODCDNIPINFO._serialized_end=2514
  _VODDESCRIBEIPINFORESULT._serialized_start=2516
  _VODDESCRIBEIPINFORESULT._serialized_end=2602
  _VODTRAFFICDATA._serialized_start=2604
  _VODTRAFFICDATA._serialized_end=2651
  _VODDESCRIBEVODDOMAINTRAFFICDATARESULT._serialized_start=2654
  _VODDESCRIBEVODDOMAINTRAFFICDATARESULT._serialized_end=2886
# @@protoc_insertion_point(module_scope)
