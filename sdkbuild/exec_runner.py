import subprocess
from subprocess import CalledProcessError

def make_call(call_args):
    error = 0;
    output = '';
    try:
        output = subprocess.check_output(call_args);
        error = 0;
    except CalledProcessError as e:
        output = e.output;
        error = e.returncode;
    return (output, error);