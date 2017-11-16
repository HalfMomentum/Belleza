import app
if app.config['TESTING']:
    print 'In testing mode'
else:
    app.config['TESTING'] = True;
    print'Entering testing mode'

"""
Making Sure the test variable in config file is set to True.
most basic task to make testing possible.
    f = tmpdir.join('config.yml')
    def test_get_config_yaml(tmpdir):
    f.write('TEST_VAR: true')

    config = get_config('app.config.Testing', yaml_files=[str(f)])

    assert config.TEST_VAR is Tr
"""
