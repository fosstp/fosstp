import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = '臺北市自由軟體數位學習資源網'
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
    'PyMySQL',
    'waitress',
    'SQLAlchemy',
    'pytest',
    'pytest-cov',
    'bcrypt',
    'Markdown',
    'feedparser'
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
      entry_points="""\
      [paste.app_factory]
      main = fosstp:main
      """,
      )
