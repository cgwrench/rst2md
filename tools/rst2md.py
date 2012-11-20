#!/usr/bin/python

"""
rst2md.py
======

This module provides a simple command line interface that uses the
Markdown writer to output from reStructuredText source.
"""

import locale
try:
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline, default_description
try:
    from docutils.writers import markdown
except ImportError:
    # Obviously still just testing this package (i.e. have not installed it)
    # Remove this try-except from the final release version.
    import sys, os
    sys.path.insert(0, os.path.abspath('.'))
    import markdown

description = ('Generates Markdown formatted text from standalone '
               'reStructuredText sources.  ' + default_description)

publish_cmdline(writer=markdown.Writer(), description=description)
