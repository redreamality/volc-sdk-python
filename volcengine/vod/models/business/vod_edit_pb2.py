# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vod/business/vod_edit.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bvod/business/vod_edit.proto\x12\x1eVolcengine.Vod.Models.Business\"0\n\x1fSubmitDirectEditTaskAsyncResult\x12\r\n\x05ReqId\x18\x01 \x01(\t\"\x97\x01\n\x13GetDirectEditResult\x12\r\n\x05ReqId\x18\x01 \x01(\t\x12\x11\n\tEditParam\x18\x02 \x01(\x0c\x12\x10\n\x08Priority\x18\x03 \x01(\x05\x12\x13\n\x0b\x43\x61llbackUri\x18\x04 \x01(\t\x12\x14\n\x0c\x43\x61llbackArgs\x18\x05 \x01(\t\x12\x0e\n\x06Status\x18\x06 \x01(\t\x12\x11\n\tOutputVid\x18\x07 \x01(\tB\xc8\x01\n)com.volcengine.service.vod.model.businessB\x07VodEditP\x01ZAgithub.com/volcengine/volc-sdk-golang/service/vod/models/business\xa0\x01\x01\xd8\x01\x01\xca\x02 Volc\\Service\\Vod\\Models\\Business\xe2\x02#Volc\\Service\\Vod\\Models\\GPBMetadatab\x06proto3')



_SUBMITDIRECTEDITTASKASYNCRESULT = DESCRIPTOR.message_types_by_name['SubmitDirectEditTaskAsyncResult']
_GETDIRECTEDITRESULT = DESCRIPTOR.message_types_by_name['GetDirectEditResult']
SubmitDirectEditTaskAsyncResult = _reflection.GeneratedProtocolMessageType('SubmitDirectEditTaskAsyncResult', (_message.Message,), {
  'DESCRIPTOR' : _SUBMITDIRECTEDITTASKASYNCRESULT,
  '__module__' : 'vod.business.vod_edit_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.SubmitDirectEditTaskAsyncResult)
  })
_sym_db.RegisterMessage(SubmitDirectEditTaskAsyncResult)

GetDirectEditResult = _reflection.GeneratedProtocolMessageType('GetDirectEditResult', (_message.Message,), {
  'DESCRIPTOR' : _GETDIRECTEDITRESULT,
  '__module__' : 'vod.business.vod_edit_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.GetDirectEditResult)
  })
_sym_db.RegisterMessage(GetDirectEditResult)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n)com.volcengine.service.vod.model.businessB\007VodEditP\001ZAgithub.com/volcengine/volc-sdk-golang/service/vod/models/business\240\001\001\330\001\001\312\002 Volc\\Service\\Vod\\Models\\Business\342\002#Volc\\Service\\Vod\\Models\\GPBMetadata'
  _SUBMITDIRECTEDITTASKASYNCRESULT._serialized_start=63
  _SUBMITDIRECTEDITTASKASYNCRESULT._serialized_end=111
  _GETDIRECTEDITRESULT._serialized_start=114
  _GETDIRECTEDITRESULT._serialized_end=265
# @@protoc_insertion_point(module_scope)
