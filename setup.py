from distutils.core import setup
import py2exe
import glob
import os

setup(
    options = {
        'py2exe': {
            'bundle_files': 2,
            'includes':['peewee','src.dependencies'],
        }
    },
    console=["gui.py"],
)
