# -*- coding: utf-8 -*-
import os
import signal
import subprocess

import pytest


@pytest.fixture(scope="module", autouse=True)
def record_vedio():
    cmd = "scrcpy --record file.mp4"
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    yield
    os.kill(p.pid, signal.CTRL_C_EVENT)
    # subprocess.Popen("cmd.exe /k taskkill /F /T /PID %i" % p.pid, shell=True)
    # print("cmd.exe /k taskkill /F /T /PID:%i" % p.pid)
    # subprocess.Popen("cmd.exe /k taskkill /F /T /PID %i" % p.pid, shell=True)
