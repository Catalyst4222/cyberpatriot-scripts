# require authentication
(Get-WmiObject -class "Win32_TSGeneralSetting" -Namespace root\cimv2\terminalservices -ComputerName $env:computername -Filter "TerminalName='RDP-tcp'").SetUserAuthenticationRequired(1)

# turn off remote desktop
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server'-name "fDenyTSConnections" -Value 1

# turn off remote assistance
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Remote Assistance'-name "fAllowToGetHelp" -Value 0

# prevent firewall
Disable-NetFirewallRule -DisplayGroup "Remote Desktop"
