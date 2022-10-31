# download chocolatey
Set-ExecutionPolicy Bypass -Scope Process -Force; 
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; 
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# download stuff with chocolatey
choco feature enable -n allowGlobalConfirmation
choco install git -y

# refresh environment
refreshenv
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine")

