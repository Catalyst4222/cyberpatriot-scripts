import pathlib
import sys
from subprocess import PIPE, run

from .parse_users import parse_readme_users
from .utils import (read_paragraph, run_powershell_command,
                    run_powershell_script)

run_powershell_command("clear")

print(
    """
███████╗██████╗  ██████╗ ███████╗████████╗██████╗ ██╗   ██╗████████╗███████╗
██╔════╝██╔══██╗██╔═══██╗██╔════╝╚══██╔══╝██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔════╝
█████╗  ██████╔╝██║   ██║███████╗   ██║   ██████╔╝ ╚████╔╝    ██║   █████╗  
██╔══╝  ██╔══██╗██║   ██║╚════██║   ██║   ██╔══██╗  ╚██╔╝     ██║   ██╔══╝  
██║     ██║  ██║╚██████╔╝███████║   ██║   ██████╔╝   ██║      ██║   ███████╗
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═════╝    ╚═╝      ╚═╝   ╚══════╝
"""
)

prompt = """Please select an option
1) Check for unauthorized users
2) Override every password
3) Update common software (Firefox, Notepad++)
4) Import LGPO

0) exit
> """
# todo: admins, firewall, services

path = pathlib.Path(__file__).parent

while True:
    choice = input(prompt)

    match choice:
        case "0":
            exit(0)
            
        case "1":
            userlist = read_paragraph(
                "Please copy/paste the user list from the readme:\n"
            ) + "\n\n" + read_paragraph()  # because of the space

            run_powershell_script(
                path / r"Disable_UnauthorizedUsers.ps1", ['"' + userlist + '"']
            )
            
        case "2":
            password = input("Choose the password to set for *every* user\n> ")
            run_powershell_script(
                path / "Set-GlobalPassword.ps1", [password]
            )
            print("\nPlease check that user passwords will expire")
            print("Currently, there's no workable automation to do it")
            
        case "3":
            run_powershell_command("choco upgrade firefox notepadplusplus")
            
        case "4":
            exe = path / "LGPO.exe"
            backup = path / "{C8610C31-85FD-49D0-9F4B-D393E80DC44C}"
            run(f"{exe} /g {backup}")
