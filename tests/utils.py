from contextlib import contextmanager
import os
import shlex
import subprocess


@contextmanager
def inside_dir(directory_path):
    """
    Run code from the context of the given directory.

    :param directory_path: The path of the directory to operate in.
    """
    current_path = os.getcwd()
    try:
        os.chdir(directory_path)
        yield
    finally:
        os.chdir(current_path)


def run_commands_inside_dir(directory_path, commands):
    """
    Run a series of commands from inside a given directory, returning the
    exit statuses

    :param directory_path: String, path of the directory the commands is being run in.
    :param commands: Command that will be executed
    """
    command_exit_codes = []
    with inside_dir(directory_path):
        for command in commands:
            command_exit_codes.append(subprocess.check_call(shlex.split(command)))

    return command_exit_codes
