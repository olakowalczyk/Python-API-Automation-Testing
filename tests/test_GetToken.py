from pyassert import *

class TestToken:
    
    def test_get_auth_token(self, token):
        """
        Checks whether token is properly returned
        """
        assert_that(token).is_not_none()
        assert len(token) == 15
