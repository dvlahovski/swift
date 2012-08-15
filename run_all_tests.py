#!/usr/bin/python
"""
A script that runs all tests sequentially.
"""
import subprocess

runner = 'gtester'
prefix = './tests/'
executables = [ 'bin64test',
                'binstest2',
                'connecttest',
                'dgramtest',
                'hashtest',
                'transfertest']

def construct_command():
    """
    Constructs command for running the tests.
    """
    command = runner
    for x in executables:
        command += ' {0}{1}'.format(prefix, x)
    return command

subprocess.call(construct_command(), shell=True)
