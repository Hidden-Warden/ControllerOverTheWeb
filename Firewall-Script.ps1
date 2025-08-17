# Ensure script is running as administrator
if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Warning "This script must be run as Administrator."
    Pause
    exit 1
}

# Get port from argument or prompt user
if ($args.Count -ge 1 -and $args[0] -match '^\d+$') {
    $RulePort = [int]$args[0]
} else {
    $RulePort = Read-Host "Enter the port number for the firewall rule"
    if ($RulePort -notmatch '^\d+$') {
        Write-Error "Invalid port number."
        exit 1
    }
    $RulePort = [int]$RulePort
}

$RuleName   = "ControllerOverTheWeb"
$RuleProto  = "UDP"

# Check if rule exists
$rule = Get-NetFirewallRule -Name $RuleName -ErrorAction SilentlyContinue

if ($null -eq $rule) {
    # Create new rule
    New-NetFirewallRule -Name $RuleName `
        -DisplayName $RuleName `
        -Direction Inbound `
        -Action Allow `
        -Protocol $RuleProto `
        -LocalPort $RulePort `
        -RemotePort Any `
        -Profile Any `
        -EdgeTraversalPolicy Allow

    Write-Output "Firewall rule '$RuleName' created on port $RulePort ($RuleProto)."
}
else {
    # Remove and recreate the rule with updated settings
    Remove-NetFirewallRule -Name $RuleName

    New-NetFirewallRule -Name $RuleName `
        -DisplayName $RuleName `
        -Direction Inbound `
        -Action Allow `
        -Protocol $RuleProto `
        -LocalPort $RulePort `
        -RemotePort Any `
        -Profile Any `
        -EdgeTraversalPolicy Allow

    Write-Output "Firewall rule '$RuleName' updated to port $RulePort ($RuleProto)."
}
