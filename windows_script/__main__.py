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
5) Enable firewall
6) Stop services
7) Set UAC to level 2
8) Secure and disable remote desktop/remote assistance

0) exit
> """
# todo: admins, services, remote desktop, remote assistance, internet properties, ?
print("Hey check sysinternals")

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
            
        case "3":
            run_powershell_command("choco upgrade firefox notepadplusplus")
            
        case "4":
            exe = path / "LGPO.exe"
            backup = path / "{C8610C31-85FD-49D0-9F4B-D393E80DC44C}"
            run(f"{exe} /g {backup}")

        case "5":
            run_powershell_command("Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True")
            
        case "6":
            to_disable = [
                "RemoteRegistry",  # Remote Registry
                "TermService",  # Remote Desktop
                "lmhosts", # TCP/IP NetBIOS Helper
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
                run_powershell_command(f"Set-Service -Name {service} -StartupType Disabled -Status Stopped")
                print(f"Stopped service {service}")

            for service in to_enable:
                run_powershell_command(f"Set-Service -Name {service} -StartupType Automatic -Status Running")
                print(f"Started service {service}")

        case "7":
            run_powershell_command(r"Import-Module .\reg.ps1; Set-UACLevel -Level 2")

        case "8":
            # secure remote desktop
            #run_powershell_command("""(Get-WmiObject -class "Win32_TSGeneralSetting" -Namespace root\cimv2\terminalservices -ComputerName $env:computername -Filter "TerminalName='RDP-tcp'").SetUserAuthenticationRequired(1)""")
            
            # disable remote desktop
            #run_powershell_command("Set-ItemProperty -Path ‘HKLM:\System\CurrentControlSet\Control\Terminal Server’-name “fDenyTSConnections” -Value 1")
            run_powershell_script(r".\rmtdsktp.ps1")

            
