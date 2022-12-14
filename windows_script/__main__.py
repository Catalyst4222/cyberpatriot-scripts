import pathlib
import sys
import os
from subprocess import PIPE, run

from .parse_users import parse_readme_users, get_admins
from .utils import read_paragraph, run_powershell_command, run_powershell_script
import io
import contextlib

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
1) Check for unauthorized users and admins
2) Override every password
3) Update common software (Firefox, Notepad++)
4) Import LGPO
5) Enable firewall
6) Stop services
7) Set UAC to level 2
8) Secure and disable remote desktop/remote assistance
9) Search for forbidden files in other user directories

0) exit
> """
# todo: services, internet properties, network shares, ?
print("Hey check sysinternals")

path = pathlib.Path(__file__).parent

while True:
    choice = input(prompt)

    match choice:
        case "0":
            exit(0)

        case "1":
            userlist = (
                read_paragraph("Please copy/paste the user list from the readme:\n")
                + "\n\n"
                + read_paragraph()
            )  # because of the space

            run_powershell_script(
                path / r"Disable_UnauthorizedUsers.ps1", ['"' + userlist + '"']
            )

            # admins
            admins = get_admins(userlist)
            # with contextlib.redirect_stdout(out):
            registered = (
                run_powershell_command(
                    r"""Get-LocalGroupMember -Group Administrators | Where-Object {Write-Host ($_.Name -split "\\")[1]}""",
                    stdout=PIPE,
                )
                .stdout.decode()
                .split("\n")
            )
            registered = [x for x in registered if x]
            print(registered)

            # Get-LocalGroupMember -Group Administrators | Where-Object {Write-Host ($_.Name -split "\\")[1]}
            bad = set(registered) - (set(registered) & set(admins))

            for baddie in bad:
                choice = input(
                    f"Remove {baddie} from the Administrators list? (Y/n)\n> "
                )
                if choice not in ("n", "N"):
                    run_powershell_command(
                        f"Remove-LocalGroupMember -Group Administrators -Member {baddie}"
                    )

        case "2":
            password = input("Choose the password to set for *every* user\n> ")
            run_powershell_script(path / "Set-GlobalPassword.ps1", [password])

        case "3":
            run_powershell_command("choco upgrade firefox notepadplusplus")

        case "4":
            exe = path / "LGPO.exe"
            backup = path / "{56112830-1CD4-4BE9-9011-39F62E012138}"
            run(f"{exe} /g {backup}")

        case "5":
            run_powershell_command(
                "Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True"
            )

        case "6":
            to_disable = [
                "RemoteRegistry",  # Remote Registry
                "TermService",  # Remote Desktop
                "lmhosts",  # TCP/IP NetBIOS Helper
                "Spooler",  # Print Spooler
                # "ssh-agent",  # OpenSSH Authentication Agent
            ]
            to_enable = [
                "Sense",  # Windows Defender Advanced Threat Protection Service
                "mpssvc",  # Windows Defender Firewall
                "EventLog",  # Windows Event Log
                "wuauserv",  # Windows Update
            ]
            for service in to_disable:
                run_powershell_command(
                    f"Set-Service -Name {service} -StartupType Disabled -Status Stopped"
                )
                print(f"Stopped service {service}")

            for service in to_enable:
                run_powershell_command(
                    f"Set-Service -Name {service} -StartupType Automatic -Status Running"
                )
                print(f"Started service {service}")

        case "7":
            run_powershell_command(r"Import-Module .\reg.ps1; Set-UACLevel -Level 2")

        case "8":
            # secure remote desktop
            # run_powershell_command("""(Get-WmiObject -class "Win32_TSGeneralSetting" -Namespace root\cimv2\terminalservices -ComputerName $env:computername -Filter "TerminalName='RDP-tcp'").SetUserAuthenticationRequired(1)""")

            # disable remote desktop
            # run_powershell_command("Set-ItemProperty -Path ‘HKLM:\System\CurrentControlSet\Control\Terminal Server’-name “fDenyTSConnections” -Value 1")
            run_powershell_script(r".\rmtdsktp.ps1")

        case "9":
            banananned = [
                "mp4",
                "mp3",
                "mac",
                "exe",
                "txt",
                "png",
                "gif",
                "jpg",
                "jpeg",
                "doc",
                "password",
            ]

            # user = input("What is the name of your user?\n> ")
            user = pathlib.Path.home().name
            for root, dirs, files in os.walk(pathlib.Path.home().parent):
                dirs[:] = [d for d in dirs if d != user]  # do dynamically
                for name in files:
                    for banned in banananned:
                        if banned in name:
                            print("Possible bad file found:")
                            print
                            # print()
                            print(os.path.join(root, name))
                            choice = input("Would you like to remove it? <Y/n>\n> ")
                            if choice not in ("n", "N"):
                                place = pathlib.Path(os.path.join(root, name))
                                place.unlink()

        case "export lgpo":
            exe = path / "LGPO.exe"
            export = path.absolute()
            run_powershell_command(f"{exe} /b {export}")

                # print(files)
