#Get all scheduled tasks on the system in a Csv format
$Tasks = schtasks /query /v /fo csv | ConvertFrom-Csv
#Filtering out all Windows tasks for Windows 2k3 and 2k12 (and 2k8?)
$ScheduledTasks = $Tasks | Where-Object { $_.HostName -eq $env:COMPUTERNAME -and $_.Author -ne "N/A" -and $_.Author -notmatch "Microsoft" -and $_.TaskName -notmatch "User_Feed_Synchronization" }
# -and $_.'Scheduled Task State' -ne "Disabled" # <-- Add this to the where-object selection in the line above to filter out disabled tasks as well
# // -and $_.'Next Run Time' -ne "N/A" 

Foreach($ScheduledTask in $ScheduledTasks)
{
    $Tasktext = ""
    $ScheduledTask.'TaskName'.Substring($ScheduledTask.'TaskName'.IndexOf("\")+1)
    $ScheduledTask.'Start In'
    $ScheduledTask.'Task To Run'
    #In case of W2k12 (and W2k8?)
    If($ScheduledTask.'Schedule Type')
    {
        Switch($ScheduledTask.'Schedule Type')
        {
            "Hourly " { $Tasktext = $ScheduledTask.'Schedule Type' + "at " + $ScheduledTask.'Start Time' }
            "Daily " { $Tasktext = $ScheduledTask.'Schedule Type' + "at " + $ScheduledTask.'Start Time' }
            "Weekly" { $Tasktext = $ScheduledTask.'Schedule Type' + " on every " + $ScheduledTask.Days + " at " + $ScheduledTask.'Start Time' }
            "Monthly"
            {
                If($ScheduledTask.Months -eq "Every month") { $Tasktext = $ScheduledTask.'Schedule Type' + " on day " + $ScheduledTask.Days + " at " + $ScheduledTask.'Start Time'}
                Else { $Tasktext = "Yearly on day " + $ScheduledTask.Days + " of " + $ScheduledTask.Months + " at " + $ScheduledTask.'Start Time' }
            }
        }
    }
    #In case of W2k3
    If($ScheduledTask.'Scheduled Type')
    {
        Switch($ScheduledTask.'Scheduled Type')
        {
            "Hourly " { $Tasktext = $ScheduledTask.'Scheduled Type' + "at " + $ScheduledTask.'Start Time' }
            "Daily " { $Tasktext = $ScheduledTask.'Scheduled Type' + "at " + $ScheduledTask.'Start Time' }
            "Weekly" { $Tasktext = $ScheduledTask.'Scheduled Type' + " on every " + $ScheduledTask.Days + " at " + $ScheduledTask.'Start Time' }
            "Monthly"
            {
                If($ScheduledTask.Months -eq "JAN,FEB,MAR,APR,MAY,JUN,JUL,AUG,SEP,OCT,NOV,DEC") { $Tasktext = $ScheduledTask.'Scheduled Type' + " on day " + $ScheduledTask.Days + " at " + $ScheduledTask.'Start Time' }
                Else { $Tasktext = "Yearly on day " + $ScheduledTask.Days + " of " + $ScheduledTask.Months + " at " + $ScheduledTask.'Start Time' }
            }
        }
    }
    #This line can be removed if the filter excludes disabled tasks
    If($ScheduledTask.'Scheduled Task State' -eq "Disabled") { $Tasktext = "Disabled" }

    $Tasktext
}