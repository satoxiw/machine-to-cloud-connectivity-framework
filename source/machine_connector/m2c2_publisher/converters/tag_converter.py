# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
import logging


class TagConverter:
    def __init__(self, protocol):
        self.protocol = protocol
        # Logging
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

    def convert_opcua_tag(self, payload):
        """
        Converting the OPC-UA alias, representing the telemetry tag
        Replacing '/' with '_' and "." with "-" in tag
        """
        self.payload = payload
        tag = self.payload["alias"].replace(".", "-").replace("/", "_")
        return tag

    def convert_opcda_tag(self, payload):
        """
        Using the alias to pull out the tag for OPC-DA
        """
        tag = payload["alias"].split('/')[-1]
        return tag

    def retrieve_tag(self, payload):
        if self.protocol == "opcua":
            self.tag = self.convert_opcua_tag(payload)
        if self.protocol == "opcda":
            self.tag = self.convert_opcda_tag(payload)
        return self.tag
