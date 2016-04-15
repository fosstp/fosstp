import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'pyramid_mailer',
    'pyramid_wtforms',
    'pyramid_tm',
    'pyramid_sqlalchemy',
    'pyramid_redis_sessions',
    'alembic',
    'deform',
    'ColanderAlchemy',
    'waitress',
    ]

setup_requires = [
    'pytest-runner',
    ]

test_requires = [
    'pytest',
    'webtest',
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
