import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = '臺北市自由軟體數位學習資源網'
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid==1.6.1',
    'pyramid_jinja2==2.6.2',
    'pyramid_debugtoolbar==2.4.2',
    'pyramid_mailer==0.14.1',
    'pyramid_wtforms==2.4.0',
    'pyramid_tm==0.12.1',
    'pyramid_sqlalchemy==1.6',
    'pyramid_redis_sessions==1.0.1',
    'alembic==0.8.6',
    'deform==2.0a2',
    'ColanderAlchemy==0.3.3',
    'mysql-connector-python==2.1.3',
    'waitress==0.9.0b1',
    ]

setup_requires = [
    'pytest-runner',
    ]

test_requires = [
    'pytest',
    'WebTest',
    'pytest-cov',
    ]

dependency_links = [
    'https://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python-2.1.3.tar.gz',
    ]

setup(name='fosstp',
      version='0.0',
      description='fosstp',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      setup_requires=setup_requires,
      tests_require=test_requires,
      dependency_links=dependency_links,
      test_suite="fosstp",
      entry_points="""\
      [paste.app_factory]
      main = fosstp:main
      """,
      )
