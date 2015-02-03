from __future__ import absolute_import
import os
import sys
import importlib

from ..Logger import *

class cmd_uninstall(object):
    
    @classmethod
    def usage(self):
        return {
            'name': 'uninstall',
            'args': '<path to files in SDK, relative to SDKROOT>',
            'desc': 'removes files to a path in the current SDK'
        };
    
    @classmethod
    def action(self, args):
        Logger.debuglog([Logger.colour('black',True), Logger.string('%s', 'uninstalling!'), Logger.colour('reset', True)]);