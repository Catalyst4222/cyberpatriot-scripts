$url = "https://www.python.org/ftp/python/3.10.7/python-3.10.7-amd64.exe" 
$output = "$HOME/Desktop/python-3.10.7-amd64.exe" 

if (Test-Path $output) { 
    Write-Host "Script exists - skipping installation" 
    return; 
} 

[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 
Invoke-WebRequest https -Uri $url -OutFile $output 

& $output /passive InstallAllUsers=1 PrependPath=1 Include_test=0 

 
