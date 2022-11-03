import pathlib
import sys
from subprocess import PIPE

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

0) exit
> """

path = pathlib.Path(__file__).parent

while True:
    choice = input(prompt)

    match choice:
        case "0":
            exit(0)
        case "1":

            userlist = read_paragraph(
                "Please copy/paste the user list:\n"
            )  # seems to work decently

            # userlist_two = read_paragraph("AAAA")  # because of the split line
            # userlist = userlist_one + "\n\n" + userlist_two
            #
            # print(userlist)
            # users, _ = parse_readme_users(userlist)
            # print(users)
            #

            run_powershell_script(
                path / r"Disable_UnauthorizedUsers.ps1", ['"' + userlist + '"']
            )
        case "2":
            password = input("Choose the password to set for *every* user\n> ")
            run_powershell_script(
                path / "Set-GlobalPassword.ps1",
            )
            print("incomplete")
