from __future__ import absolute_import
import os
import sys
import argparse
import readline
import rlcompleter

from .Logger import *
from .commandparse import InputHandler
from .settings import Settings

# Main
def main():
    if 'libedit' in readline.__doc__:
        readline.parse_and_bind("bind ^I rl_complete");
    else:
        readline.parse_and_bind("tab: complete");
    
    config = Settings();
    if config.CheckForConfigAndInit() == True:
        config.ConfigureForXcodeInstall();
        sdkbuilder = InputHandler();
        sdkbuilder.settings = config;
        sdkbuilder.cmdloop();
    else:
        Logger.debuglog([Logger.colour('red',True), Logger.string('%s', 'Error'), Logger.colour('reset', True), Logger.string('%s', ': Could setup preferences file!')]);

if __name__ == "__main__":
    main();