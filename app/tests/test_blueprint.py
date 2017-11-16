
import sys

from flask import current_app



def test_index_200():
    """Makes sure the front page returns HTTP 200.
    A very basic test, if the front page is broken, something has obviously failed.
    """
    assert '200 OK' == current_app.test_client().get('/').status
test_index_200()
"""
Checks if our index page at any time returns 400 bad REQUEST.
"""
def test_bad_request():
    assert '400 BAD REQUEST' == current_app.test_client().get('/examples/alerts/modal').status
    assert '400 BAD REQUEST' == current_app.test_client().get('/examples/alerts/modal?flash_type=success').status

def test_assert_404(self):
    """
    Checks if our index page at any time returns 404 oops.
    """
    self.assert404(self.client.get("/oops/"))

def test_assert_403(self):
    """
    Checks if our index page at any time returns 403 Forbidden.
    """
    self.assert403(self.client.get("/forbidden/"))

def test_assert_401(self):
    """
    Checks if our index page at any time returns 401 unauthorized.
    Redirects to login page.
    """
    self.assert401(self.client.get("/unauthorized/"))

def test_assert_405(self):
    """
    Checks if our index page at any time returns 405.
    """
    self.assert405(self.client.post("/"))

def test_assert_500(self):
    """
    Checks if our index page at any time returns 500 internal server error.
    """
    self.assert500(self.client.get("/internal_server_error/"))
