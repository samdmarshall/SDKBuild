from __future__ import absolute_import
import os
import importlib

from ..Logger import *

class cmd_info(object):
    
    @classmethod
    def usage(self):
        return {
            'name': 'info',
            'args': '',
            'desc': 'Displays current configuration info'
        };
    
    @classmethod
    def action(self, args):
        Logger.debuglog([Logger.colour('black',True), Logger.string('%s', 'Info:'), Logger.colour('reset', True)]);