from rest_framework import status

"""
  Log entry schemas used for tests in apps/logging/tests/test_audit_loggers.py
  See the following for information about the JSON Schema vocabulary: https://json-schema.org/
"""

FHIR_PAT_ID_STR = "patientId:-20140000008325"

ACCESS_TOKEN_AUTHORIZED_LOG_SCHEMA = {
    "title": "AccessTokenAuthorizedLogSchema",
    "type": "object",
    "properties": {
        "type": {"pattern": "AccessToken"},
        "action": {"pattern": "authorized"},
        "auth_grant_type": {"pattern": "password"},
        "id": {"type": "integer"},
        "scopes": {"pattern": "read write patient"},
        "user": {
            "type": "object",
            "properties": {"id": {"type": "integer"}, "username": {"pattern": "John"}},
        },
        "crosswalk": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "user_hicn_hash": {
                    "pattern": "96228a57f37efea543f4f370f96f1dbf01c3e3129041dba3ea4367545507c6e7"
                },
                "user_mbi_hash": {
                    "pattern": "98765432137efea543f4f370f96f1dbf01c3e3129041dba3ea43675987654321"
                },
                "fhir_id": {"pattern": "-20140000008325"},
                "user_id_type": {"pattern": "H"},
            },
        },
    },
    "required": [
        "type",
        "action",
        "auth_grant_type",
        "id",
        "scopes",
        "user",
        "crosswalk",
    ],
}

AUTHENTICATION_START_LOG_SCHEMA = {
    "title": "AuthenticationStartLogSchema",
    "type": "object",
    "properties": {
        "type": {"pattern": "Authentication:start"},
        "sls_status": {"pattern": "OK"},
        "sls_status_mesg": {"type": "null"},
        "sub": {"pattern": "00112233-4455-6677-8899-aabbccddeeff"},
        "sls_mbi_format_valid": {"type": "boolean"},
        "sls_mbi_format_msg": {"pattern": "Valid"},
        "sls_mbi_format_synthetic": {"type": "boolean"},
        "sls_hicn_hash": {
            "pattern": "f7dd6b126d55a6c49f05987f4aab450deae3f990dcb5697875fd83cc61583948"
        },
        "sls_mbi_hash": {
            "pattern": "4da2e5f86b900604651c89e51a68d421612e8013b6e3b4d5df8339d1de345b28"
        },
        "sls_signout_status_code": {"type": "integer", "enum": [status.HTTP_302_FOUND]},
        "sls_token_status_code": {"type": "integer", "enum": [status.HTTP_200_OK]},
        "sls_userinfo_status_code": {"type": "integer", "enum": [status.HTTP_200_OK]},
        "sls_validate_signout_status_code": {
            "type": "integer",
            "enum": [status.HTTP_403_FORBIDDEN],
        },
    },
    "required": [
        "type",
        "sls_status",
        "sls_status_mesg",
        "sub",
        "sls_mbi_format_valid",
        "sls_mbi_format_synthetic",
        "sls_hicn_hash",
        "sls_mbi_hash",
        "sls_signout_status_code",
        "sls_token_status_code",
        "sls_userinfo_status_code",
        "sls_validate_signout_status_code",
    ],
}

AUTHENTICATION_SUCCESS_LOG_SCHEMA = {
    "title": "AuthenticationSuccessLogSchema",
    "type": "object",
    "properties": {
        "type": {"pattern": "Authentication:success"},
        "sub": {"pattern": "00112233-4455-6677-8899-aabbccddeeff"},
        "user": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "username": {"pattern": "00112233-4455-6677-8899-aabbccddeeff"},
                "crosswalk": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "user_hicn_hash": {
                            "pattern": "f7dd6b126d55a6c49f05987f4aab450deae3f990dcb5697875fd83cc61583948"
                        },
                        "user_mbi_hash": {
                            "pattern": "4da2e5f86b900604651c89e51a68d421612e8013b6e3b4d5df8339d1de345b28"
                        },
                        "fhir_id": {"pattern": "-20140000008325"},
                        "user_id_type": {"pattern": "M"},
                    },
                },
            },
        },
        "auth_crosswalk_action": {"pattern": "C"},
    },
    "required": ["type", "sub", "user", "auth_crosswalk_action"],
}

AUTHORIZATION_LOG_SCHEMA = {
    "title": "AuthorizationLogSchema",
    "type": "object",
    "properties": {
        "type": {"pattern": "Authorization"},
        "auth_status": {"pattern": "OK"},
        "auth_status_code": {"type": "null"},
        "user": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "username": {"pattern": "anna"},
                "crosswalk": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "user_hicn_hash": {
                            "pattern": "96228a57f37efea543f4f370f96f1dbf01c3e3129041dba3ea4367545507c6e7"
                        },
                        "user_mbi_hash": {
                            "pattern": "98765432137efea543f4f370f96f1dbf01c3e3129041dba3ea43675987654321"
                        },
                        "fhir_id": {"pattern": "-20140000008325"},
                        "user_id_type": {"pattern": "H"},
                    },
                },
            },
        },
        "application": {
            "type": "object",
            "properties": {"id": {"pattern": "1"}, "name": {"pattern": "an app"}},
        },
        "share_demographic_scopes": {"pattern": "^$"},
        "scopes": {"pattern": "capability-a"},
        "allow": {"type": "boolean"},
        "access_token_delete_cnt": {"type": "integer", "enum": [0]},
        "refresh_token_delete_cnt": {"type": "integer", "enum": [0]},
        "data_access_grant_delete_cnt": {"type": "integer", "enum": [0]},
        "auth_uuid": {"type": "string", "format": "uuid"},
        "auth_client_id": {"type": "string"},
        "auth_app_id": {"pattern": "^1$"},
        "auth_app_name": {"pattern": "an app"},
        "auth_app_data_access_type": {"pattern": "ONE_TIME"},
        "auth_pkce_method": {"type": "null"},
        "auth_share_demographic_scopes": {"pattern": "^$"},
        "auth_require_demographic_scopes": {"pattern": "^True$"},
    },
    "required": [
        "type",
        "auth_status",
        "auth_status_code",
        "user",
        "application",
        "share_demographic_scopes",
        "scopes",
        "allow",
        "access_token_delete_cnt",
        "refresh_token_delete_cnt",
        "data_access_grant_delete_cnt",
        "auth_uuid",
        "auth_client_id",
        "auth_app_id",
        "auth_app_name",
        "auth_app_data_access_type",
        "auth_pkce_method",
        "auth_share_demographic_scopes",
        "auth_require_demographic_scopes",
    ],
}

FHIR_AUTH_POST_FETCH_LOG_SCHEMA = {
    "title": "FhirAuthPostFetchLogSchema",
    "type": "object",
    "properties": {
        "type": {"pattern": "fhir_auth_post_fetch"},
        "uuid": {"type": "string"},
        "includeAddressFields": {"pattern": "False"},
        "path": {"pattern": "patient search"},
        "start_time": {"type": "string"},
        "code": {"type": "integer", "enum": [status.HTTP_200_OK]},
        "size": {"type": "integer"},
        "elapsed": {"type": "number"},
    },
    "required": [
        "type",
        "uuid",
        "includeAddressFields",
        "path",
        "start_time",
        "code",
        "size",
        "elapsed",
    ],
}

FHIR_AUTH_PRE_FETCH_LOG_SCHEMA = {
    "title": "FhirAuthPreFetchLogSchema",
    "type": "object",
    "properties": {
        "type": {"pattern": "fhir_auth_pre_fetch"},
        "uuid": {"type": "string"},
        "includeAddressFields": {"pattern": "False"},
        "path": {"pattern": "patient search"},
        "start_time": {"type": "string"},
    },
    "required": ["type", "uuid", "includeAddressFields", "path", "start_time"],
}


def get_post_fetch_fhir_log_entry_schema(version):
    return {
        "title": "FhirPostFetchLogSchema",
        "type": "object",
        "properties": {
            "type": {"pattern": "fhir_post_fetch"},
            "uuid": {"type": "string"},
            "fhir_id": {"pattern": "-20140000008325"},
            "includeAddressFields": {"pattern": "False"},
            "user": {"pattern": FHIR_PAT_ID_STR},
            "application": {
                "type": "object",
                "properties": {
                    "id": {"pattern": "1"},
                    "name": {"pattern": "John_Smith_test"},
                    "user": {"type": "object", "properties": {"id": {"pattern": "1"}}},
                },
            },
            "path": {"pattern": "/v{}/fhir/Patient".format(version)},
            "start_time": {"type": "string"},
            "code": {"type": "integer", "enum": [status.HTTP_200_OK]},
            "size": {"type": "integer"},
            "elapsed": {"type": "number"},
        },
        "required": [
            "type",
            "uuid",
            "fhir_id",
            "includeAddressFields",
            "user",
            "application",
            "path",
            "start_time",
            "code",
            "size",
            "elapsed",
        ],
    }


def get_pre_fetch_fhir_log_entry_schema(version):
    return {
        "title": "FhirPreFetchLogSchema",
        "type": "object",
        "properties": {
            "type": {"pattern": "fhir_pre_fetch"},
            "uuid": {"type": "string"},
            "fhir_id": {"pattern": "-20140000008325"},
            "includeAddressFields": {"pattern": "False"},
            "user": {"pattern": FHIR_PAT_ID_STR},
            "application": {
                "type": "object",
                "properties": {
                    "id": {"pattern": "1"},
                    "name": {"pattern": "John_Smith_test"},
                    "user": {"type": "object", "properties": {"id": {"pattern": "1"}}},
                },
            },
            "path": {"pattern": "/v{}/fhir/Patient".format(version)},
            "start_time": {"type": "string"},
        },
        "required": [
            "type",
            "uuid",
            "fhir_id",
            "includeAddressFields",
            "user",
            "application",
            "path",
            "start_time",
        ],
    }


MATCH_FHIR_ID_LOG_SCHEMA = {
    "title": "MatchFhirIdLogSchema",
    "type": "object",
    "properties": {
        "type": {
            "type": "string",
            "pattern": "^fhir.server.authentication.match_fhir_id$",
        },
        "auth_uuid": {"type": "null"},
        "auth_app_id": {"type": "null"},
        "auth_app_name": {"type": "null"},
        "auth_app_data_access_type": {"pattern": "RESEARCH_STUDY"},
        "auth_client_id": {"type": "null"},
        "auth_pkce_method": {"type": "null"},
        "fhir_id": {"type": "string", "pattern": "^-20140000008325$"},
        "hicn_hash": {
            "type": "string",
            "pattern": "^f7dd6b126d55a6c49f05987f4aab450deae3f990dcb5697875fd83cc61583948$",
        },
        "mbi_hash": {
            "type": "string",
            "pattern": "^4da2e5f86b900604651c89e51a68d421612e8013b6e3b4d5df8339d1de345b28$",
        },
        "match_found": {"type": "boolean"},
        "hash_lookup_type": {"type": "string", "pattern": "^M$"},
        "hash_lookup_mesg": {
            "type": "string",
            "pattern": "^FOUND beneficiary via mbi_hash$",
        },
    },
    "required": [
        "type",
        "auth_uuid",
        "auth_app_id",
        "auth_app_name",
        "auth_app_data_access_type",
        "auth_client_id",
        "auth_pkce_method",
        "fhir_id",
        "hicn_hash",
        "mbi_hash",
        "match_found",
        "hash_lookup_type",
        "hash_lookup_mesg",
    ],
}

MYMEDICARE_CB_CREATE_BENE_LOG_SCHEMA = {
    "title": "MyMedicareCbCreateBeneLogSchema",
    "type": "object",
    "properties": {
        "type": {"pattern": "mymedicare_cb:create_beneficiary_record"},
        "status": {"pattern": "OK"},
        "username": {"pattern": "00112233-4455-6677-8899-aabbccddeeff"},
        "fhir_id": {"pattern": "-20140000008325"},
        "user_mbi_hash": {
            "pattern": "4da2e5f86b900604651c89e51a68d421612e8013b6e3b4d5df8339d1de345b28"
        },
        "user_hicn_hash": {
            "pattern": "f7dd6b126d55a6c49f05987f4aab450deae3f990dcb5697875fd83cc61583948"
        },
        "mesg": {"pattern": "CREATE beneficiary record"},
    },
    "required": [
        "type",
        "status",
        "username",
        "fhir_id",
        "user_mbi_hash",
        "user_hicn_hash",
        "mesg",
    ],
}

MYMEDICARE_CB_GET_UPDATE_BENE_LOG_SCHEMA = {
    "title": "MyMedicareCbGetUpdateBeneLogSchema",
    "type": "object",
    "properties": {
        "type": {"type": "string", "pattern": "^mymedicare_cb:get_and_update_user$"},
        "status": {"type": "string", "pattern": "^OK$"},
        "subject": {
            "type": "string",
            "pattern": "^00112233-4455-6677-8899-aabbccddeeff$",
        },
        "user_username": {
            "type": "string",
            "pattern": "^00112233-4455-6677-8899-aabbccddeeff$",
        },
        "fhir_id": {"type": "string", "pattern": "^-20140000008325$"},
        "hicn_hash": {
            "type": "string",
            "pattern": "^f7dd6b126d55a6c49f05987f4aab450deae3f990dcb5697875fd83cc61583948$",
        },
        "mbi_hash": {
            "type": "string",
            "pattern": "^4da2e5f86b900604651c89e51a68d421612e8013b6e3b4d5df8339d1de345b28$",
        },
        "hash_lookup_type": {"type": "string", "pattern": "^M$"},
        "crosswalk": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "user_hicn_hash": {
                    "type": "string",
                    "pattern": "^f7dd6b126d55a6c49f05987f4aab450deae3f990dcb5697875fd83cc61583948$",
                },
                "user_mbi_hash": {
                    "type": "string",
                    "pattern": "^4da2e5f86b900604651c89e51a68d421612e8013b6e3b4d5df8339d1de345b28$",
                },
                "fhir_id": {"type": "string", "pattern": "^-20140000008325$"},
                "user_id_type": {"type": "string", "pattern": "^M$"},
            },
        },
        "hicn_updated": {"enum": [False]},
        "mbi_updated": {"enum": [False]},
        "mbi_updated_from_null": {"enum": [False]},
        "mesg": {"type": "string", "pattern": "^CREATE beneficiary record$"},
        "request_uuid": {"type": "string"},
        "crosswalk_before": {
            "type": "object",
            "properties": {},
        },
    },
    "required": [
        "type",
        "status",
        "subject",
        "user_username",
        "fhir_id",
        "hicn_hash",
        "mbi_hash",
        "crosswalk",
        "hicn_updated",
        "mbi_updated",
        "mbi_updated_from_null",
        "mesg",
        "request_uuid",
        "crosswalk_before",
    ],
}

REQUEST_RESPONSE_MIDDLEWARE_LOG_SCHEMA = {
    "title": "RequestResponseLogSchema",
    "type": "object",
    "properties": {
        "type": {"pattern": "request_response_middleware"},
        "size": {"type": "integer"},
        "start_time": {"type": "number"},
        "end_time": {"type": "number"},
        "ip_addr": {"type": "string", "format": "ip-address"},
        "request_uuid": {"type": "string", "format": "uuid"},
        "req_user_id": {"type": "integer", "enum": [1]},
        "req_user_username": {"pattern": "00112233-4455-6677-8899-aabbccddeeff"},
        "req_fhir_id": {"pattern": "-20140000008325"},
        "auth_crosswalk_action": {"pattern": "C"},
        "path": {"pattern": "/mymedicare/sls-callback"},
        "request_method": {"pattern": "GET"},
        "request_scheme": {"pattern": "http"},
        "user": {"pattern": "00112233-4455-6677-8899-aabbccddeeff"},
        "fhir_id": {"pattern": "-20140000008325"},
        "response_code": {"type": "integer", "enum": [status.HTTP_302_FOUND]},
    },
    "required": [
        "type",
        "size",
        "start_time",
        "end_time",
        "ip_addr",
        "request_uuid",
        "req_user_id",
        "req_user_username",
        "req_fhir_id",
        "auth_crosswalk_action",
        "path",
        "request_method",
        "request_scheme",
        "user",
        "fhir_id",
        "response_code",
    ],
}

REQUEST_PARTIAL_LOG_REC_SCHEMA = {
    "title": "RequestResponseLogSchemaPartial",
    "type": "object",
    "properties": {
        "type": {"pattern": "request_response_middleware"},
        "size": {"type": "integer"},
        "start_time": {"type": "number"},
        "end_time": {"type": "number"},
        "ip_addr": {"type": "string", "format": "ip-address"},
        "request_uuid": {"type": "string", "format": "uuid"},
        "req_qparam_client_id": {"type": "string"},
        "req_app_id": {"type": "string"},
        "req_app_name": {"type": "string"},
        "path": {"enum": ["/v1/o/authorize/", "/v2/o/authorize/"]},
        "request_method": {"pattern": "GET"},
        "request_scheme": {"pattern": "http"},
        "response_code": {"type": "integer"},
    },
    "required": [
        "type",
        "size",
        "start_time",
        "end_time",
        "ip_addr",
        "request_uuid",
        "req_qparam_client_id",
        "req_app_id",
        "req_app_name",
        "path",
        "request_method",
        "request_scheme",
        "response_code",
    ],
}

SLSX_TOKEN_LOG_SCHEMA = {
    "title": "SlsxTokenLogSchema",
    "type": "object",
    "properties": {
        "type": {"pattern": "SLSx_token"},
        "uuid": {"type": "string"},
        "path": {"pattern": "/sso/session"},
        "auth_token": {"type": "string"},
        "code": {"type": "integer", "enum": [status.HTTP_200_OK]},
        "size": {"type": "integer"},
        "start_time": {"type": "string"},
        "elapsed": {"type": "number"},
    },
    "required": [
        "type",
        "uuid",
        "path",
        "auth_token",
        "code",
        "size",
        "start_time",
        "elapsed",
    ],
}

SLSX_USERINFO_LOG_SCHEMA = {
    "title": "SlsxUserInfoLogSchema",
    "type": "object",
    "properties": {
        "type": {"pattern": "SLSx_userinfo"},
        "uuid": {"type": "string"},
        "path": {"pattern": "/v1/users/00112233-4455-6677-8899-aabbccddeeff"},
        "sub": {"pattern": "00112233-4455-6677-8899-aabbccddeeff"},
        "code": {"type": "integer", "enum": [status.HTTP_200_OK]},
        "size": {"type": "integer"},
        "start_time": {"type": "string"},
        "elapsed": {"type": "number"},
    },
    "required": [
        "type",
        "uuid",
        "path",
        "sub",
        "code",
        "size",
        "start_time",
        "elapsed",
    ],
}

"""
  Log entry schema used for tests in apps/logging/tests/test_loggers_management_command.py
"""
GLOBAL_STATE_METRICS_LOG_SCHEMA = {
    "title": "GlobalStateMetrics",
    "type": "object",
    "properties": {
        "type": {"pattern": "global_state_metrics"},
        "group_timestamp": {"type": "string"},
        "real_bene_cnt": {"type": "integer"},
        "synth_bene_cnt": {"type": "integer"},
        "crosswalk_real_bene_count": {"type": "integer"},
        "crosswalk_synthetic_bene_count": {"type": "integer"},
        "crosswalk_table_count": {"type": "integer"},
        "crosswalk_archived_table_count": {"type": "integer"},
        "crosswalk_bene_counts_elapsed": {"type": "number"},
        "grant_real_bene_count": {"type": "integer"},
        "grant_synthetic_bene_count": {"type": "integer"},
        "grant_table_count": {"type": "integer"},
        "grant_archived_table_count": {"type": "integer"},
        "grant_counts_elapsed": {"type": "number"},
        "grant_real_bene_deduped_count": {"type": "integer"},
        "grant_synthetic_bene_deduped_count": {"type": "integer"},
        "grant_deduped_counts_elapsed": {"type": "number"},
        "grantarchived_real_bene_deduped_count": {"type": "integer"},
        "grantarchived_synthetic_bene_deduped_count": {"type": "integer"},
        "grantarchived_deduped_counts_elapsed": {"type": "number"},
        "grant_and_archived_real_bene_deduped_count": {"type": "integer"},
        "grant_and_archived_synthetic_bene_deduped_count": {"type": "integer"},
        "grant_and_archived_deduped_counts_elapsed": {"type": "number"},
        "token_real_bene_deduped_count": {"type": "integer"},
        "token_synthetic_bene_deduped_count": {"type": "integer"},
        "token_real_bene_app_pair_deduped_count": {"type": "integer"},
        "token_synthetic_bene_app_pair_deduped_count": {"type": "integer"},
        "token_table_count": {"type": "integer"},
        "token_archived_table_count": {"type": "integer"},
        "token_deduped_counts_elapsed": {"type": "number"},
        "global_apps_active_cnt": {"type": "integer"},
        "global_apps_inactive_cnt": {"type": "integer"},
        "global_apps_require_demographic_scopes_cnt": {"type": "integer"},
        "global_state_metrics_total_elapsed": {"type": "number"},
        "global_developer_count": {"type": "number"},
        "global_developer_with_registered_app_count": {"type": "number"},
        "global_developer_with_first_api_call_count": {"type": "number"},
        "global_developer_distinct_organization_name_count": {"type": "number"},
        "global_beneficiary_count": {"type": "number"},
        "global_beneficiary_real_count": {"type": "number"},
        "global_beneficiary_synthetic_count": {"type": "number"},
        "global_beneficiary_grant_count": {"type": "number"},
        "global_beneficiary_real_grant_count": {"type": "number"},
        "global_beneficiary_synthetic_grant_count": {"type": "number"},
        "global_beneficiary_grant_archived_count": {"type": "number"},
        "global_beneficiary_real_grant_archived_count": {"type": "number"},
        "global_beneficiary_synthetic_grant_archived_count": {"type": "number"},
        "global_beneficiary_grant_or_archived_count": {"type": "number"},
        "global_beneficiary_real_grant_or_archived_count": {"type": "number"},
        "global_beneficiary_synthetic_grant_or_archived_count": {"type": "number"},
        "global_beneficiary_grant_and_archived_count": {"type": "number"},
        "global_beneficiary_real_grant_and_archived_count": {"type": "number"},
        "global_beneficiary_synthetic_grant_and_archived_count": {"type": "number"},
        "global_beneficiary_grant_not_archived_count": {"type": "number"},
        "global_beneficiary_real_grant_not_archived_count": {"type": "number"},
        "global_beneficiary_synthetic_grant_not_archived_count": {"type": "number"},
        "global_beneficiary_archived_not_grant_count": {"type": "number"},
        "global_beneficiary_real_archived_not_grant_count": {"type": "number"},
        "global_beneficiary_synthetic_archived_not_grant_count": {"type": "number"},
        "global_beneficiary_real_grant_to_apps_eq_1_count": {"type": "number"},
        "global_beneficiary_synthetic_grant_to_apps_eq_1_count": {"type": "number"},
        "global_beneficiary_real_grant_to_apps_eq_2_count": {"type": "number"},
        "global_beneficiary_synthetic_grant_to_apps_eq_2_count": {"type": "number"},
        "global_beneficiary_real_grant_to_apps_eq_3_count": {"type": "number"},
        "global_beneficiary_synthetic_grant_to_apps_eq_3_count": {"type": "number"},
        "global_beneficiary_real_grant_to_apps_eq_4thru5_count": {"type": "number"},
        "global_beneficiary_synthetic_grant_to_apps_eq_4thru5_count": {"type": "number"},
        "global_beneficiary_real_grant_to_apps_eq_6thru8_count": {"type": "number"},
        "global_beneficiary_synthetic_grant_to_apps_eq_6thru8_count": {"type": "number"},
        "global_beneficiary_real_grant_to_apps_eq_9thru13_count": {"type": "number"},
        "global_beneficiary_synthetic_grant_to_apps_eq_9thru13_count": {"type": "number"},
        "global_beneficiary_real_grant_to_apps_gt_13_count": {"type": "number"},
        "global_beneficiary_synthetic_grant_to_apps_gt_13_count": {"type": "number"},
        "global_beneficiary_real_grant_archived_to_apps_eq_1_count": {"type": "number"},
        "global_beneficiary_synthetic_grant_archived_to_apps_eq_1_count": {"type": "number"},
        "global_beneficiary_real_grant_archived_to_apps_eq_2_count": {"type": "number"},
        "global_beneficiary_synthetic_grant_archived_to_apps_eq_2_count": {"type": "number"},
        "global_beneficiary_real_grant_archived_to_apps_eq_3_count": {"type": "number"},
        "global_beneficiary_synthetic_grant_archived_to_apps_eq_3_count": {"type": "number"},
        "global_beneficiary_real_grant_archived_to_apps_eq_4thru5_count": {"type": "number"},
        "global_beneficiary_synthetic_grant_archived_to_apps_eq_4thru5_count": {"type": "number"},
        "global_beneficiary_real_grant_archived_to_apps_eq_6thru8_count": {"type": "number"},
        "global_beneficiary_synthetic_grant_archived_to_apps_eq_6thru8_count": {"type": "number"},
        "global_beneficiary_real_grant_archived_to_apps_eq_9thru13_count": {"type": "number"},
        "global_beneficiary_synthetic_grant_archived_to_apps_eq_9thru13_count": {"type": "number"},
        "global_beneficiary_real_grant_archived_to_apps_gt_13_count": {"type": "number"},
        "global_beneficiary_synthetic_grant_archived_to_apps_gt_13_count": {"type": "number"},
        "global_beneficiary_counts_elapsed": {"type": "number"},
        "global_beneficiary_app_pair_grant_count": {"type": "number"},
        "global_beneficiary_app_pair_real_grant_count": {"type": "number"},
        "global_beneficiary_app_pair_synthetic_grant_count": {"type": "number"},
        "global_beneficiary_app_pair_grant_archived_count": {"type": "number"},
        "global_beneficiary_app_pair_real_grant_archived_count": {"type": "number"},
        "global_beneficiary_app_pair_synthetic_grant_archived_count": {"type": "number"},
        "global_beneficiary_app_pair_grant_vs_archived_difference_total_count": {"type": "number"},
        "global_beneficiary_app_pair_real_grant_vs_archived_difference_total_count": {"type": "number"},
        "global_beneficiary_app_pair_synthetic_grant_vs_archived_difference_total_count": {"type": "number"},
        "global_beneficiary_app_pair_archived_vs_grant_difference_total_count": {"type": "number"},
        "global_beneficiary_app_pair_real_archived_vs_grant_difference_total_count": {"type": "number"},
        "global_beneficiary_app_pair_synthetic_archived_vs_grant_difference_total_count": {"type": "number"},
        "global_beneficiary_app_pair_counts_elapsed": {"type": "number"},
    },
    "required": [
        "type",
        "group_timestamp",
        "real_bene_cnt",
        "synth_bene_cnt",
        "crosswalk_real_bene_count",
        "crosswalk_synthetic_bene_count",
        "crosswalk_table_count",
        "crosswalk_archived_table_count",
        "crosswalk_bene_counts_elapsed",
        "grant_real_bene_count",
        "grant_synthetic_bene_count",
        "grant_table_count",
        "grant_archived_table_count",
        "grant_counts_elapsed",
        "grant_real_bene_deduped_count",
        "grant_synthetic_bene_deduped_count",
        "grant_deduped_counts_elapsed",
        "grantarchived_real_bene_deduped_count",
        "grantarchived_synthetic_bene_deduped_count",
        "grantarchived_deduped_counts_elapsed",
        "grant_and_archived_real_bene_deduped_count",
        "grant_and_archived_synthetic_bene_deduped_count",
        "grant_and_archived_deduped_counts_elapsed",
        "token_real_bene_deduped_count",
        "token_synthetic_bene_deduped_count",
        "token_table_count",
        "token_archived_table_count",
        "token_real_bene_app_pair_deduped_count",
        "token_synthetic_bene_app_pair_deduped_count",
        "token_deduped_counts_elapsed",
        "global_apps_active_cnt",
        "global_apps_inactive_cnt",
        "global_apps_require_demographic_scopes_cnt",
        "global_state_metrics_total_elapsed",
        "global_developer_count",
        "global_developer_with_registered_app_count",
        "global_developer_with_first_api_call_count",
        "global_developer_distinct_organization_name_count",
        "global_developer_counts_elapsed",
        "global_beneficiary_count",
        "global_beneficiary_real_count",
        "global_beneficiary_synthetic_count",
        "global_beneficiary_grant_count",
        "global_beneficiary_real_grant_count",
        "global_beneficiary_synthetic_grant_count",
        "global_beneficiary_grant_archived_count",
        "global_beneficiary_real_grant_archived_count",
        "global_beneficiary_synthetic_grant_archived_count",
        "global_beneficiary_grant_or_archived_count",
        "global_beneficiary_real_grant_or_archived_count",
        "global_beneficiary_synthetic_grant_or_archived_count",
        "global_beneficiary_grant_and_archived_count",
        "global_beneficiary_real_grant_and_archived_count",
        "global_beneficiary_synthetic_grant_and_archived_count",
        "global_beneficiary_grant_not_archived_count",
        "global_beneficiary_real_grant_not_archived_count",
        "global_beneficiary_synthetic_grant_not_archived_count",
        "global_beneficiary_archived_not_grant_count",
        "global_beneficiary_real_archived_not_grant_count",
        "global_beneficiary_synthetic_archived_not_grant_count",
        "global_beneficiary_real_grant_to_apps_eq_1_count",
        "global_beneficiary_synthetic_grant_to_apps_eq_1_count",
        "global_beneficiary_real_grant_to_apps_eq_2_count",
        "global_beneficiary_synthetic_grant_to_apps_eq_2_count",
        "global_beneficiary_real_grant_to_apps_eq_3_count",
        "global_beneficiary_synthetic_grant_to_apps_eq_3_count",
        "global_beneficiary_real_grant_to_apps_eq_4thru5_count",
        "global_beneficiary_synthetic_grant_to_apps_eq_4thru5_count",
        "global_beneficiary_real_grant_to_apps_eq_6thru8_count",
        "global_beneficiary_synthetic_grant_to_apps_eq_6thru8_count",
        "global_beneficiary_real_grant_to_apps_eq_9thru13_count",
        "global_beneficiary_synthetic_grant_to_apps_eq_9thru13_count",
        "global_beneficiary_real_grant_to_apps_gt_13_count",
        "global_beneficiary_synthetic_grant_to_apps_gt_13_count",
        "global_beneficiary_real_grant_archived_to_apps_eq_1_count",
        "global_beneficiary_synthetic_grant_archived_to_apps_eq_1_count",
        "global_beneficiary_real_grant_archived_to_apps_eq_2_count",
        "global_beneficiary_synthetic_grant_archived_to_apps_eq_2_count",
        "global_beneficiary_real_grant_archived_to_apps_eq_3_count",
        "global_beneficiary_synthetic_grant_archived_to_apps_eq_3_count",
        "global_beneficiary_real_grant_archived_to_apps_eq_4thru5_count",
        "global_beneficiary_synthetic_grant_archived_to_apps_eq_4thru5_count",
        "global_beneficiary_real_grant_archived_to_apps_eq_6thru8_count",
        "global_beneficiary_synthetic_grant_archived_to_apps_eq_6thru8_count",
        "global_beneficiary_real_grant_archived_to_apps_eq_9thru13_count",
        "global_beneficiary_synthetic_grant_archived_to_apps_eq_9thru13_count",
        "global_beneficiary_real_grant_archived_to_apps_gt_13_count",
        "global_beneficiary_synthetic_grant_archived_to_apps_gt_13_count",
        "global_beneficiary_counts_elapsed",
        "global_beneficiary_app_pair_grant_count",
        "global_beneficiary_app_pair_real_grant_count",
        "global_beneficiary_app_pair_synthetic_grant_count",
        "global_beneficiary_app_pair_grant_archived_count",
        "global_beneficiary_app_pair_real_grant_archived_count",
        "global_beneficiary_app_pair_synthetic_grant_archived_count",
        "global_beneficiary_app_pair_grant_vs_archived_difference_total_count",
        "global_beneficiary_app_pair_real_grant_vs_archived_difference_total_count",
        "global_beneficiary_app_pair_synthetic_grant_vs_archived_difference_total_count",
        "global_beneficiary_app_pair_archived_vs_grant_difference_total_count",
        "global_beneficiary_app_pair_real_archived_vs_grant_difference_total_count",
        "global_beneficiary_app_pair_synthetic_archived_vs_grant_difference_total_count",
        "global_beneficiary_app_pair_counts_elapsed",
    ],
}

"""
  Log entry schema used for tests in apps/logging/tests/test_loggers_management_command.py
"""
GLOBAL_STATE_METRICS_PER_APP_LOG_SCHEMA = {
    "title": "GlobalStatePerAppMetrics",
    "type": "object",
    "properties": {
        "type": {"pattern": "global_state_metrics_per_app"},
        "group_timestamp": {"type": "string"},
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "created": {"type": "string"},
        "updated": {"type": "string"},
        "active": {"type": "boolean"},
        "first_active": {"type": "null"},
        "last_active": {"type": "null"},
        "data_access_type": {"type": "string"},
        "require_demographic_scopes": {"type": "boolean"},
        "real_bene_cnt": {"type": "integer"},
        "synth_bene_cnt": {"type": "integer"},
        "grant_real_bene_count": {"type": "integer"},
        "grant_synthetic_bene_count": {"type": "integer"},
        "grant_table_count": {"type": "integer"},
        "grant_archived_table_count": {"type": "integer"},
        "grantarchived_real_bene_deduped_count": {"type": "integer"},
        "grantarchived_synthetic_bene_deduped_count": {"type": "integer"},
        "grant_and_archived_real_bene_deduped_count": {"type": "integer"},
        "grant_and_archived_synthetic_bene_deduped_count": {"type": "integer"},
        "token_real_bene_count": {"type": "integer"},
        "token_synthetic_bene_count": {"type": "integer"},
        "token_table_count": {"type": "integer"},
        "token_archived_table_count": {"type": "integer"},
        "token_deduped_counts_elapsed": {"type": "number"},
        "user_id": {"type": "integer"},
        "user_username": {"type": "string"},
        "user_date_joined": {"type": "string"},
        "user_last_login": {"type": "null"},
        "user_organization": {"type": "string"},
        "user_limit_data_access": {"type": "boolean"},
    },
    "required": [
        "type",
        "group_timestamp",
        "id",
        "name",
        "created",
        "updated",
        "active",
        "first_active",
        "last_active",
        "data_access_type",
        "require_demographic_scopes",
        "real_bene_cnt",
        "synth_bene_cnt",
        "grant_real_bene_count",
        "grant_synthetic_bene_count",
        "grant_table_count",
        "grant_archived_table_count",
        "grantarchived_real_bene_deduped_count",
        "grantarchived_synthetic_bene_deduped_count",
        "grant_and_archived_real_bene_deduped_count",
        "grant_and_archived_synthetic_bene_deduped_count",
        "token_real_bene_count",
        "token_synthetic_bene_count",
        "token_table_count",
        "token_archived_table_count",
        "user_id",
        "user_username",
        "user_date_joined",
        "user_last_login",
        "user_organization",
        "user_limit_data_access",
    ],
}
