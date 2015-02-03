from __future__ import absolute_import
import os
import importlib
import cmd

from ..Logger import *

from .cmd_quit import *
from .cmd_list import *
from .cmd_sdk import *
from .cmd_xcode import *
from .cmd_info import *
from .cmd_install import *
from .cmd_uninstall import *

from ..settings.Settings import Settings

class InputHandler(cmd.Cmd):
    prompt = ':> ';
    
    def GetArguments(self, arguments_str):
        arg_words = [];
        input_split = arguments_str.split(' ');
        offset = 0;
        counter = 0;
        current_word = '';
        while counter < len(input_split):
            word = input_split[counter];
            current_word += word;
            if len(current_word) == 0:
                offset += 1;
            else:
                if offset >= 0:
                    curr = offset + len(word);
                    prev = curr - 1
                    if arguments_str[prev:curr] != '\\':
                        arg_words.append(current_word);
                        current_word = '';
                    else:
                        current_word += ' ';
                    offset += len(word) + 1;
            counter += 1;
        return arg_words;
    
    def DisplayUsage(self, cmd_usage):
        Logger.debuglog([Logger.colour('black',True), Logger.string('%s', 'Command:'), Logger.colour('reset', True)]);
        Logger.debuglog([Logger.colour('black',True), Logger.string('%10s', cmd_usage['name']), Logger.string(' %s', cmd_usage['args']), Logger.string('\n%10s', '-'), Logger.string(' %s\n', cmd_usage['desc']), Logger.colour('reset', True)]);
    
    # Quit
    def help_quit(self):
        self.DisplayUsage(cmd_quit.usage());
    
    def do_quit(self, line):
        cmd_quit.action(self.GetArguments(str(line)));
    
    # List
    def help_list(self):
        self.DisplayUsage(cmd_list.usage());
    
    def do_list(self, line):
        cmd_list.action(self.settings);
    
    # SDK
    def help_sdk(self):
        self.DisplayUsage(cmd_sdk.usage());
    
    def do_sdk(self, line):
        args = self.GetArguments(str(line));
        
        if len(args) > 0:
            select_sdk = args[0];
            selected_sdk_path = '';
            for item in self.settings.ListOfActiveSDKs():
                if select_sdk == os.path.basename(item):
                    selected_sdk_path = item;
            
            cmd_sdk.action(selected_sdk_path);
    
    def complete_sdk(self, text, line, begidx, endidx):
        SDKs = [];
        for item in self.settings.ListOfActiveSDKs():
            SDKs.append(os.path.basename(item));
        
        if not text:
            completions = SDKs[:]
        else:
            completions = [ item
                            for item in SDKs
                            if item.startswith(text)
                          ]
        return completions
    
    # Xcode
    def help_xcode(self):
        self.DisplayUsage(cmd_xcode.usage());
    
    def do_xcode(self, line):
        cmd_xcode.action(self.GetArguments(str(line)));
    
    # info
    def help_info(self):
        self.DisplayUsage(cmd_info.usage());
    
    def do_info(self, line):
        cmd_info.action(self.GetArguments(str(line)));
    
    # install
    def help_install(self):
        self.DisplayUsage(cmd_install.usage());
    
    def do_install(self, line):
        cmd_install.action(self.GetArguments(str(line)));
    
    # uninstall
    def help_install(self):
        self.DisplayUsage(cmd_uninstall.usage());
    
    def do_install(self, line):
        cmd_uninstall.action(self.GetArguments(str(line)));