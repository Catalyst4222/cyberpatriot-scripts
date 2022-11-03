param($password=$false)

function Set-GlobalPassword {
    param($password)

    $pass = ConvertTo-SecureString -String $password -AsPlainText -Force

    foreach ($user in Get-LocalUser) {
        Set-LocalUser -SID $user.SID -Password $pass -PasswordNeverExpires $false -AccountExpires
    }

    Write-Host "Make sure to check expiration dates and lockouts!"
}

if($password) {
    Set-GlobalPassword $password
}