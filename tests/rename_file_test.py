import pytest
import sys
import os
sys.path.insert(1, os.getcwd())
from src.rename_files import rename
import shutil

class TestRenameFilesTest:
    def test_alltxt(self):
        path = "/Users/user/Documents/cise337-hw2-python-application-wepeng07/tests/test1 copy/"
        rename(path)
        files = os.listdir(path)
        corrects = os.listdir("/Users/user/Documents/cise337-hw2-python-application-wepeng07/tests/test1correct")
        correct_files = []
        for file in corrects:
            if os.path.isdir(file): continue
            correct_files.append(file)
        for i in range(len(files)):
            assert files[i] == correct_files[i]
    def test_with_other_files(self):
        path = "/Users/user/Documents/cise337-hw2-python-application-wepeng07/tests/test2 copy/"
        rename(path)
        files = os.listdir(path)
        corrects = os.listdir("/Users/user/Documents/cise337-hw2-python-application-wepeng07/tests/test2 correct")
        correct_files = []
        for file in corrects:
            if os.path.isdir(file): continue
            correct_files.append(file)
        for i in range(len(files)):
            assert files[i] == correct_files[i]
    def test_with_dir(self):
        path = "/Users/user/Documents/cise337-hw2-python-application-wepeng07/tests/test3 copy/"
        rename(path)
        files = os.listdir(path)
        corrects = os.listdir("/Users/user/Documents/cise337-hw2-python-application-wepeng07/tests/test3 correct")
        correct_files = []
        for file in corrects:
            if os.path.isdir(file): continue
            correct_files.append(file)
        for i in range(len(files)):
            assert files[i] == correct_files[i]

