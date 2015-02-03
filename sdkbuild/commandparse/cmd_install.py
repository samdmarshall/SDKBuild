from __future__ import absolute_import
import os
import sys
import importlib

from ..Logger import *

class cmd_install(object):
    
    @classmethod
    def usage(self):
        return {
            'name': 'install',
            'args': '<path to files> <path to files in SDK, relative to SDKROOT>',
            'desc': 'installs files to a path in the current SDK'
        };
    
    @classmethod
    def action(self, args):
        Logger.debuglog([Logger.colour('black',True), Logger.string('%s', 'installing!'), Logger.colour('reset', True)]);