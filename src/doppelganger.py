from pathlib import Path
from tqdm import tqdm
import os
import sys
import fire


def main():
    if len(sys.argv) == 1:
        usage()
    else:
        fire.Fire(doppelganger)


def usage():
    msg = '''\
    INFO: Showing help with the command option '--help' or '-h'.

    NAME
        doppelganger.py - Create a file with an alternative extension from an
        original file.

    SYNOPSIS
        doppelganger.py ALTERNATIVE_FILE_EXTENSION <flags>

    DESCRIPTION
        Create a file with an alternative extension from an original file.

    POSITIONAL ARGUMENTS
        ALTERNATIVE_FILE_EXTENSION
            A name of the file extension you want to create.

    FLAGS
        --target_directory=TARGET_DIRECTORY
            A directory containing the original file.
        --td=TD
            A shortened option for target_directory.
        --original_file_extention=ORIGINAL_FILE_EXTENTION
        --ofe=OFE
            A shortened option for original_file_extension.
        --output_directory=OUTPUT_DIRECTORY
            A directory to output the file with an alternative extension.
        --od=OD
            A shortened option for ouput_directory.

    NOTES
        You can also use flags syntax for POSITIONAL ARGUMENTS
    '''
    print(msg)


def doppelganger(alternative_file_extension,
                 target_directory="",
                 td="",
                 original_file_extention="",
                 ofe="",
                 output_directory="",
                 od=""):
    """Create a file with an alternative extension from an original file.

    :param alternative_file_extension: A name of the file extension
    you want to create.
    :param target_directory: A directory containing the original file.
    :param td: A shortened option for target_directory.
    :param original_file_extension: The original file extension
    you want to target.
    :param ofe: A shortened option for original_file_extension.
    :param output_directory: A directory to output the file
    with an alternative extension.
    :param od: A shortened option for ouput_directory.

    """
    target_dirpath = "."
    output_dirpath = "."
    target_file_list = []
    dot_original_file_extension = ""
    dot_alternative_file_extension = "." + alternative_file_extension

    for tmp_target_directory in [target_directory, td]:
        if tmp_target_directory != "":
            if isExistsDir(tmp_target_directory):
                target_dirpath = os.path.expandvars(tmp_target_directory)
                target_dirpath = os.path.expanduser(target_dirpath)
            else:
                sys.exit()

    for tmp_original_file_extension in [original_file_extention, ofe]:
        if tmp_original_file_extension != "":
            dot_original_file_extension = "." + tmp_original_file_extension

    for tmp_output_directory in [output_directory, od]:
        if tmp_output_directory != "":
            if isExistsDir(tmp_output_directory, errMsg=False):
                output_dirpath = os.path.expandvars(tmp_output_directory)
                output_dirpath = os.path.expanduser(output_dirpath)
            else:
                output_dirpath = os.path.expandvars(tmp_output_directory)
                output_dirpath = os.path.expanduser(output_dirpath)
                os.makedirs(output_dirpath, exist_ok=True)

    target_file_list = [
        file for file in os.listdir(target_dirpath)
        if os.path.isfile(os.path.join(target_dirpath, file))
    ]
    tmp_target_file_list = target_file_list

    if dot_original_file_extension != "":
        target_file_list = [
            os.path.splitext(file)[0] for file in tmp_target_file_list
            if os.path.splitext(file)[1] == dot_original_file_extension
        ]
    else:
        target_file_list = [
            os.path.splitext(file)[0] for file in tmp_target_file_list
        ]

    print("Start creating doppelganger.")
    for file in tqdm(target_file_list):
        output_file = os.path.join(output_dirpath,
                                   file + dot_alternative_file_extension)
        Path(output_file).touch()
        print("Created : " + output_file)
    print("Complete!")


def isExistsDir(dirpath, errMsg=True):
    if dirpath != "":
        tmp_dirpath = os.path.expandvars(dirpath)
        tmp_dirpath = os.path.expanduser(tmp_dirpath)
        if os.path.exists(tmp_dirpath) is not True:
            if errMsg:
                print("The specified directory is not found.")
            return False

        if os.path.isdir(tmp_dirpath) is not True:
            if errMsg:
                print("The specified directory is not a directory.")
            return False

    return True


if __name__ == "__main__":
    main()
