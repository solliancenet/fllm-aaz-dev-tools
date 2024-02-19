from unittest import TestCase
from command.model.configuration._condition import *
from command.tests.common import verify_xml


class ConditionTest(TestCase):

    def test_has_value_operator(self):
        operator = CMDConditionHasValueOperator({
            "type": "hasValue",
            "arg": "$arg1"
        })
        assert operator.type == "hasValue"
        assert operator.arg == "$arg1"
        operator.validate()
        operator.to_native()
        operator.to_primitive()

        verify_xml(self, operator)

    def test_operators(self):
        operator = CMDConditionAndOperator({
            "type": "and",
            "operators": [
                {
                    "type": "not",
                    "operator": {
                        "type": "hasValue",
                        "arg": "$arg1"
                    }
                },
                {
                    "type": "or",
                    "operators": [
                        {
                            "type": "hasValue",
                            "arg": "$arg3",
                        },
                        {
                            "type": "hasValue",
                            "arg": "$arg2"
                        }
                    ]
                }
            ]
        })
        assert operator.type == CMDConditionAndOperator.TYPE_VALUE
        assert len(operator.operators) == 2
        assert operator.operators[0].type == CMDConditionNotOperator.TYPE_VALUE
        assert operator.operators[0].operator.type == CMDConditionHasValueOperator.TYPE_VALUE
        assert operator.operators[1].type == CMDConditionOrOperator.TYPE_VALUE
        assert len(operator.operators[1].operators) == 2
        operator.validate()
        operator.to_native()
        operator.to_primitive()

        verify_xml(self, operator)

    def test_condition(self):
        condition = CMDCondition(
            {
                "var": "$condition_1",
                "operator": {
                    "type": "and",
                    "operators": [
                        {
                            "type": "not",
                            "operator": {
                                "type": "hasValue",
                                "arg": "$arg1"
                            }
                        },
                        {
                            "type": "or",
                            "operators": [
                                {
                                    "type": "hasValue",
                                    "arg": "$arg3",
                                },
                                {
                                    "type": "hasValue",
                                    "arg": "$arg2"
                                }
                            ]
                        }
                    ]
                }
            }
        )
        condition.validate()
        condition.to_native()
        condition.to_primitive()

        verify_xml(self, condition)

