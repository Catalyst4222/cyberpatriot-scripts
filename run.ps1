# The main entry point for the script
Write-Host "
███████╗██████╗  ██████╗ ███████╗████████╗██████╗ ██╗   ██╗████████╗███████╗
██╔════╝██╔══██╗██╔═══██╗██╔════╝╚══██╔══╝██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔════╝
█████╗  ██████╔╝██║   ██║███████╗   ██║   ██████╔╝ ╚████╔╝    ██║   █████╗  
██╔══╝  ██╔══██╗██║   ██║╚════██║   ██║   ██╔══██╗  ╚██╔╝     ██║   ██╔══╝  
██║     ██║  ██║╚██████╔╝███████║   ██║   ██████╔╝   ██║      ██║   ███████╗
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═════╝    ╚═╝      ╚═╝   ╚══════╝
"

Write-Host "Welcome! Before we get started, there are a few things we have to go over first"

if(!((Read-Host "Have you done the forensics questions? (y/N)") -eq "y")) {
    Write-Host "Go do those first smh"
    Read-Host
    exit
}

$prompt = "Please select an option:
1) Check for unauthorized users

0) exit
"

while ($true) {
    $choice = Read-Host $prompt

    if($choice -eq "0") {
      exit 0
    }
}