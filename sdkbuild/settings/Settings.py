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
        
        sdkbuild_config_file = os.path.join(sdkbuild_dir_path, 'config.plist');
        
        status = os.path.exists(sdkbuild_config_file);
        if status == False:
            print 'create the plist';
        
        status = os.path.exists(sdkbuild_config_file);
        if status == False:
            return status;
        
        print 'read the plist';
        
        return status;
    
    def ConfigureForXcodeInstall(self):
        print ''