import os
import pathlib
import subprocess
import sys
from typing import Union


def run_powershell_command(command: str | list[str], /, *args, **kwargs):
    if isinstance(command, str):
        command = [command]
    return subprocess.run(["powershell", "-Command", *command], *args, **kwargs)


def run_powershell_script(
    script: Union[str, pathlib.Path, os.PathLike],
    extras: list[str] = (),
    /,
    *args,
    **kwargs,
):
    if isinstance(script, os.PathLike):
        script = script.__fspath__()
    script = str(script)

    print(f"{extras=!r}")
    return subprocess.run(["powershell", script, *extras], *args, **kwargs)


def read_paragraph(prompt: str = ""):
    print(prompt, end="")
    res = ""
    while data := input():
        res += data
        res += "\n"
    return res
