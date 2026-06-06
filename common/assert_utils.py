import pytest
def assert_msg(resp,msg):
    assert resp.json().get("msg") == msg

def assert_code(resp,expected_code):
    assert resp.json().get("code") == expected_code

def assert_state_code(resp,expected_state_code):
    assert resp.status_code == expected_state_code



