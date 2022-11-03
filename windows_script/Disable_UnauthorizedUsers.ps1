# todo turn into a proper script
param($userlist=$false)


function Disable-UnauthorizedUsers {
    param (
        $users
    )

    foreach ($user in Get-LocalUser) {
        #Write-Host $users.Contains($user.Name)
        if((!$users.Contains($user.Name)) -and $user.Enabled){
            Write-Host "Bad user found!"
            Write-Host $user.Name
            if((Read-Host "Do you want to disable this user? (y/n)") -eq "y"){
                Write-Host "Disabling user..."
                Disable-LocalUser $user.SID
            }
        }
    }
}


if($userlist) {
    Disable-UnauthorizedUsers $userlist
}