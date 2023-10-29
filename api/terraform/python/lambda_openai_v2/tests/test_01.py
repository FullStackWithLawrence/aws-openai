import pytest
from openai_utils.tests.test_init import get_event, handle_event


class TestOpenAIText:
    def test_basic_request(self):
        """Test a basic request"""
        event = get_event("tests/events/test_01.request.json")
        retval = handle_event(event=event)
        print(retval)

        assert retval["statusCode"] == 200
        assert isinstance(retval["body"], str)
