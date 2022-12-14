$path = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2"

#protected mode"
New-ItemProperty -Path $path -Name "2500" -Value 0


