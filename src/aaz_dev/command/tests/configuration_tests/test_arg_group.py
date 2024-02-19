from unittest import TestCase
from command.model.configuration._arg_group import *
from command.tests.common import verify_xml


class ArgumentGroupTest(TestCase):

    def test_arg_group(self):
        arg_group = CMDArgGroup({
            "name": "Destinations",
            "args": [
                {
                    "var": "$logAnalytics",
                    "options": [
                        "--log-analytics",
                    ],
                    "type": "array<object>",
                    "format": {
                        "minLength": 1,
                    },
                    "help": {
                        "short": "List of Log Analytics destinations."
                    },
                    "item": {
                        "type": "object",
                        "args": [
                            {
                                "var": "$logAnalytics[].workspaceResourceId",
                                "options": [
                                    "workspace"
                                ],
                                "type": "string",
                                "required": True,
                                "help": {
                                    "short": "The resource ID of the Log Analytics workspace.",
                                }
                            },
                            {
                                "var": "$logAnalytics[].name",
                                "options": [
                                    "name"
                                ],
                                "type": "string",
                                "required": True,
                                "help": {
                                    "short": "A friendly name for the destination.",
                                    "lines": [
                                        "This name should be unique across all destinations (regardless of type) within the data collection rule."
                                    ]
                                }
                            }
                        ]
                    }
                }
            ]
        })

        arg_group.validate()
        arg_group.to_native()
        arg_group.to_primitive()

        verify_xml(self, arg_group)
