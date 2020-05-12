from pyassert import *


def test_get_auth_token(token):
    # Tests
    assert_that(token).is_not_none()
    assert len(token) == 15
