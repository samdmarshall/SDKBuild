from __future__ import absolute_import
import os
import importlib

from ..Logger import *

class cmd_list(object):
    
    @classmethod
    def usage(self):
        return {
            'name': 'list',
            'args': '',
            'desc': 'Displays SDKS for selected Xcode Install'
        };
    
    @classmethod
    def action(self, args):
        Logger.debuglog([Logger.colour('black',True), Logger.string('%s', 'SDKs:'), Logger.colour('reset', True)]);