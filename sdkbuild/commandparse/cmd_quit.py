from __future__ import absolute_import
import os
import sys
import importlib

from ..Logger import *

class cmd_quit(object):
    
    @classmethod
    def usage(self):
        return {
            'name': 'quit',
            'args': '',
            'desc': 'Quits sdkbuild'
        };
    
    @classmethod
    def action(self, args):
        Logger.debuglog([Logger.colour('black',True), Logger.string('%s', 'Quitting!'), Logger.colour('reset', True)]);
        sys.exit();