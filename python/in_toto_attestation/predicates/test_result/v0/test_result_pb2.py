# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: in_toto_attestation/predicates/test_result/v0/test_result.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from in_toto_attestation.v1 import resource_descriptor_pb2 as in__toto__attestation_dot_v1_dot_resource__descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?in_toto_attestation/predicates/test_result/v0/test_result.proto\x12-in_toto_attestation.predicates.test_result.v0\x1a\x30in_toto_attestation/v1/resource_descriptor.proto\"\xae\x01\n\nTestResult\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x41\n\rconfiguration\x18\x02 \x03(\x0b\x32*.in_toto_attestation.v1.ResourceDescriptor\x12\x0b\n\x03url\x18\x03 \x01(\t\x12\x14\n\x0cpassed_tests\x18\x04 \x03(\t\x12\x14\n\x0cwarned_tests\x18\x05 \x03(\t\x12\x14\n\x0c\x66\x61iled_tests\x18\x06 \x03(\tBu\n6io.github.intoto.attestation.predicates.test_result.v0Z;github.com/in-toto/attestation/go/predicates/test_result/v0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'in_toto_attestation.predicates.test_result.v0.test_result_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n6io.github.intoto.attestation.predicates.test_result.v0Z;github.com/in-toto/attestation/go/predicates/test_result/v0'
  _globals['_TESTRESULT']._serialized_start=165
  _globals['_TESTRESULT']._serialized_end=339
# @@protoc_insertion_point(module_scope)
