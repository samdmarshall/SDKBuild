from __future__ import absolute_import
import os
import importlib

from ..Logger import *
from ..settings.Settings import *

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
        
        sdks = args.ListOfActiveSDKs();
        
        for sdk in sdks:
            active = ' ';
            if args.ActiveSDKPath(sdk):
                active = '*';
            
            name = os.path.basename(sdk);
            Logger.debuglog([Logger.colour('green',True), Logger.string('\t %s ', active), Logger.colour('black',True), Logger.string('%s', name), Logger.colour('reset', True)]);