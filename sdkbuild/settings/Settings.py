from __future__ import absolute_import
import os
import importlib


class Settings(object):
    
    def CheckForConfigAndInit(self):
        status = False;
        
        config_dir_path = os.path.join(os.path.expanduser('~'), '.config');
        
        status = os.path.exists(config_dir_path);
        if status == False:
            return status;
        
        sdkbuild_dir_path = os.path.join(config_dir_path, 'sdkbuild');
        
        status = os.path.exists(sdkbuild_dir_path);
        if status == False:
            os.mkdir(sdkbuild_dir_path);
        
        status = os.path.exists(sdkbuild_dir_path);
        if status == False:
            return status;
        
        
        
        return status;
    
    def ConfigureForXcodeInstall(self):
        print ''