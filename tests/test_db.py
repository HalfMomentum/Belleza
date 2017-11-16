"""
Checking if you can login as a Admin or not.
checking with 3 diff id and passwords.
"""

def test_login_logout(self):
    rv = self.login('admin', 'default')
    assert b'You were logged in' in rv.data
    rv = self.logout()
    assert b'You were logged out' in rv.data
    rv = self.login('adminx', 'default')
    assert b'Invalid username' in rv.data
    rv = self.login('admin', 'defaultx')
    assert b'Invalid password' in rv.data


"""
Fetching usernames and password from a dictionary and then checking it in the login function.
Login function can be used with both the local dictionary and OAuth.
"""

def login(self, username, password):
    return self.app.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)

def logout(self):
    return self.app.get('/logout', follow_redirects=True)
