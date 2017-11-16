# """
# Making Sure the test variable in config file is set to True.
# most basic task to make testing possible.
# """
# def test_get_config_yaml(tmpdir):
#     f = tmpdir.join('config.yml')
#     f.write('TEST_VAR: true')
#
#     config = get_config('pypi_portal.config.Testing', yaml_files=[str(f)])
#
#     assert config.TEST_VAR is True
from app import app
import os

if app.config['TESTING']:
    print 'In testing mode'
else:
    app.config['TESTING'] = True;
    print'Entering testing mode'
