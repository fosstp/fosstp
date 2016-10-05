import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = '臺北市自由軟體數位學習資源網'
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid==1.7.3',
    'pyramid_jinja2==2.6.2',
    'pyramid_debugtoolbar==3.0.4',
    'pyramid_mailer==0.14.1',
    'pyramid_wtforms==2.4.0',
    'pyramid_tm==1.0',
    'pyramid_sqlalchemy==1.6',
    'pyramid_redis_sessions==1.0.1',
    'alembic==0.8.8',
    'PyMySQL==0.7.9',
    'waitress==1.0.0',
    'SQLAlchemy==1.0.15',
    ]

setup_requires = [
    'pytest-runner',
    ]

test_requires = [
    'pytest',
    'WebTest',
    'pytest-cov',
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
      test_suite="fosstp",
      entry_points="""\
      [paste.app_factory]
      main = fosstp:main
      """,
      )
