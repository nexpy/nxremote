#!/usr/bin/env python 
# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------
# Copyright (c) 2013-2016, NeXpy Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING, distributed with this software.
#-----------------------------------------------------------------------------

__package_name__ = u'nxremote'
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

__documentation_author__ = u'Justin Wozniak'
__documentation_copyright__ = u'2013-2016, Justin Wozniak'

__license__ = u'BSD'
__author_name__ = u'NeXpy Development Team'
__author_email__ = u'nexpydev@gmail.com'
__author__ = __author_name__ + u' <' + __author_email__ + u'>'

__url__          = u'http://nexpy.github.io/nexpy/'
__download_url__ = u'https://github.com/nexpy/nxremote/'

__description__ = u'nxremote: Python API to access remote NeXus data'
__long_description__ = \
u"""
This package provides a Python API to access `NeXus data 
<http://www.nexusformat.org/>`_ written in the HDF5 format on a remote server 
across a network. The 'nexusformat' package provides the underlying API for 
`NeXpy <http://nexpy.github.io/nexpy>`_, which provides a GUI interface. 

The latest development version is always available from `NeXpy's GitHub
site <https://github.com/nexpy/nxremote>`_.
"""
