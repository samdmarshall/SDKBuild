from __future__ import absolute_import
import os
import importlib

from ..Logger import *

class cmd_xcode(object):
    
    @classmethod
    def usage(self):
        return {
            'name': 'xcode',
            'args': '<Path to Xcode.app>',
            'desc': 'Selects a Xcode install'
        };
    
    @classmethod
    def action(self, args):
        if len(args) > 0:
            xcode_path = args[0];
            Logger.debuglog([Logger.colour('black',True), Logger.string('%s', 'Select Xcode install at path: "'), Logger.string('%s', xcode_path), Logger.string('%s', '"'),  Logger.colour('reset', True)]);
        else:
            Logger.debuglog([Logger.colour('black',True), Logger.string('%s', 'Please supply the path to an installation of "Xcode.app"'), Logger.colour('reset', True)]);