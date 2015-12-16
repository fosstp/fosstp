#!/usr/bin/env python3
import sys
from pyramid.paster import get_appsettings
from sqlalchemy import engine_from_config
from sqlalchemy.ext.declarative import declarative_base

if len(sys.argv) < 2:
    print('Usage: create_db.py <ini_file>')
    exit(1)

config_file = sys.argv[1]
settings = get_appsettings(config_file)

BaseObject = declarative_base()
from osstp.models import *

engine = engine_from_config(settings, 'sqlalchemy.')
BaseObject.metadata.create_all(engine)
