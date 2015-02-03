from __future__ import absolute_import
import os
import importlib

from ..Logger import *

class cmd_sdk(object):
    
    @classmethod
    def usage(self):
        return {
            'name': 'sdk',
            'args': '<SDK Name>',
            'desc': 'Selects a SDK'
        };
    
    @classmethod
    def action(self, args):
        if len(args) > 0:
            sdk_name = args;
            Logger.debuglog([Logger.colour('black',True), Logger.string('%s', 'Selected SDK: "'), Logger.string('%s', sdk_name), Logger.string('%s', '"'), Logger.colour('reset', True)]);
            
        else:
            Logger.debuglog([Logger.colour('black',True), Logger.string('%s', 'Please supply the name of an SDK'), Logger.colour('reset', True)]);