from pyramid.paster import get_app, setup_logging
# change this setting to meet your needs
ini_path = '/YOUR/INI/PATH/production.ini'
setup_logging(ini_path)
application = get_app(ini_path, 'main')
