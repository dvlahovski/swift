#!/usr/bin/python
"""
Makes a report based on the already runned tests.
"""
import subprocess

files = [ 'bin64.cpp',
          'bingrep.cpp',
          'bins.cpp',
          'channel.cpp',
          'compat.cpp',
          'datagram.cpp',
          'hashtree.cpp',
          'httpgw.cpp',
          'send_control.cpp',
          'sendrecv.cpp',
          'swift.cpp',
          'transfer.cpp', ]

comm = ['gcov']
comm.extend(files)
subprocess.call(comm)
subprocess.call('lcov -o rawreport -c -d .', shell=True)
subprocess.call('genhtml -o result rawreport', shell=True)
