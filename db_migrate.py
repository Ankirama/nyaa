#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from nyaa import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
	# Patch sys.argv to default to 'db'
	sys.argv.insert(1, 'db')

	manager.run()
