from __future__ import absolute_import
import os
import importlib
import plistlib
import Foundation

from ..exec_runner import *

# Globals
kSDKSettingsPlistName = 'SDKSettings.plist';

class Settings(object):
    
    def PlistLoad(self, path):
        plist_dict = {};
        plistNSData, errorMessage = Foundation.NSData.dataWithContentsOfFile_options_error_(path, Foundation.NSUncachedRead, None);
        if errorMessage == None:
            plistContents, plistFormat, errorMessage = Foundation.NSPropertyListSerialization.propertyListFromData_mutabilityOption_format_errorDescription_(plistNSData, Foundation.NSPropertyListMutableContainers, None, None);
            if errorMessage == None:
                plist_dict = plistContents;
        return plist_dict;
    
    def GetSDKCanonicalName(self, sdk_path):
        sdk_settings_plist_path = os.path.join(sdk_path, kSDKSettingsPlistName);
        sdk_settings_plist = self.PlistLoad(sdk_settings_plist_path);
        return sdk_settings_plist['CanonicalName'];
    
    def ActiveSDKPath(self, path):
        path_name = self.GetSDKCanonicalName(path);
        return path_name == self.config_dict['selectedSDK'];
    
    def FindSDKsForPlatformPath(self, platform):
        found_sdks = [];
        
        dev_dir = os.path.join(platform, 'Developer');
        status = os.path.exists(dev_dir);
        if status == False:
            return found_sdks;
        
        sdk_dir = os.path.join(dev_dir, 'SDKs');
        status = os.path.exists(sdk_dir);
        if status == False:
            return found_sdks;
        
        for name in os.listdir(sdk_dir):
            path = os.path.join(sdk_dir, name)
            is_sym_link = os.path.islink(path)
            
            if name.endswith('.sdk') and is_sym_link == False:
                found_sdks.append(path);
        
        return found_sdks
    
    def XcodePlatformsDir(self):
        return os.path.join(self.config_dict['selectedXcodeInstall'], 'Platforms');
    
    def ListOfActiveSDKs(self):
        platforms = self.XcodePlatformsDir();
        
        active_sdks = [];
        
        for name in os.listdir(platforms):
            if name.endswith('.platform'):
                found_sdks = self.FindSDKsForPlatformPath(os.path.join(platforms, name));
                if len(found_sdks):
                    active_sdks.extend(found_sdks);
        
        return active_sdks;
    
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
            xcode_app_path = '';
            sdk_name = '';
            
            locate_xcode_result = make_call(('xcode-select', '-p'));
            if locate_xcode_result[1] != 0:
                status = False;
            else:
                xcode_app_path = locate_xcode_result[0].rstrip('\n');
            
            locate_sdk_results = make_call(('xcrun',  '--show-sdk-path'));
            if locate_sdk_results[1] != 0:
                status = False;
            else:
                sdk_path_dir = locate_sdk_results[0].rstrip('\n');
                sdk_name = self.GetSDKCanonicalName(sdk_path_dir);
            
            default_settings = dict(
                selectedXcodeInstall=xcode_app_path,
                selectedSDK=sdk_name
            );
            plistlib.writePlist(default_settings, sdkbuild_config_file);
        
        status = os.path.exists(sdkbuild_config_file);
        if status == False:
            return status;
        
        return status;
    
    def ConfigureForXcodeInstall(self):
        
        sdkbuild_config_file = os.path.join(os.path.expanduser('~'), '.config/sdkbuild/config.plist');
        
        self.config_dict = self.PlistLoad(sdkbuild_config_file);
        
        print self.config_dict;
        # validate that the values aren't empty