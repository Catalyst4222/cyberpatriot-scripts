import subprocess

def run_powershell(command: str | list[str], *args, **kwargs):
    if isinstance(command, str):
        command = [command]
    return subprocess.run(["powershell", "-Command", *command], *args, **kwargs)
