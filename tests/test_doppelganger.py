import glob
import os
import shutil

from src.doppelganger import doppelganger, isExistsDir


def test_doppelganger():
    pre_file_list = [
        file for file in os.listdir("tests")
        if os.path.isfile(os.path.join("tests", file))
    ]
    pre_file_count = len(pre_file_list)

    doppelganger("testdoppelganger", "tests", "", "", "", "tests", "")
    now_file_list = [
        file for file in os.listdir("tests")
        if os.path.isfile(os.path.join("tests", file))
    ]
    now_file_count = len(now_file_list)
    assert pre_file_count == now_file_count / 2
    for file in glob.glob("tests/*.testdoppelganger"):
        os.remove(file)

    doppelganger("testdoppelganger", "tests", "", "", "", "tests/subtests", "")
    now_file_list = [
        file for file in os.listdir("tests/subtests")
        if os.path.isfile(os.path.join("tests/subtests", file))
    ]
    now_file_count = len(now_file_list)
    assert pre_file_count == now_file_count
    shutil.rmtree("tests/subtests")

    doppelganger("testdoppelganger", "tests", "", "targetdoppelganger", "",
                 "tests", "")
    target_file_list = [
        file for file in os.listdir("tests")
        if os.path.isfile(os.path.join("tests", file))
    ]
    tmp_target_file_list = target_file_list
    target_file_list = [
        os.path.splitext(file)[0] for file in tmp_target_file_list
        if os.path.splitext(file)[1] == ".targetdoppelganger"
    ]
    assert len(target_file_list) == 0


def test_isExistsDir():
    assert isExistsDir("")
    assert isExistsDir(".")
    assert isExistsDir("../")
    assert isExistsDir("$HOME")
    assert isExistsDir("../doppelganger")
    assert not isExistsDir("hogehoge")
    assert not isExistsDir("doppelganger.py")
