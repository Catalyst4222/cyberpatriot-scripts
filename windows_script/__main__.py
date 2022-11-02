import sys
from .utils import run_powershell
from .parse_users import parse_readme

from subprocess import PIPE

run_powershell("clear")

print("""
███████╗██████╗  ██████╗ ███████╗████████╗██████╗ ██╗   ██╗████████╗███████╗
██╔════╝██╔══██╗██╔═══██╗██╔════╝╚══██╔══╝██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔════╝
█████╗  ██████╔╝██║   ██║███████╗   ██║   ██████╔╝ ╚████╔╝    ██║   █████╗  
██╔══╝  ██╔══██╗██║   ██║╚════██║   ██║   ██╔══██╗  ╚██╔╝     ██║   ██╔══╝  
██║     ██║  ██║╚██████╔╝███████║   ██║   ██████╔╝   ██║      ██║   ███████╗
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═════╝    ╚═╝      ╚═╝   ╚══════╝
""")

prompt = """Please select an option
1) Check for unauthorized users

0) exit
> """

while True:
    choice = input(prompt)

    match choice:
        case "0":
            exit(0)
        case "1":
            print("Please copy/paste the user list")
            
            userlist = 
            process = run_powershell([".\Disable_UnauthorizedUsers.ps1"])
            print(process)

    print("A")
