#!/usr/bin/python3
'''
Reloads storage
'''
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
