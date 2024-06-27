<# 
PowerShell version of Termite Credential Hunter
Made with love 
2xdropout 2024
#>

$matchValues = @("creds", "credentials", "password","passwd", "logon")
$ctfIndicatorValues = @("ctf","flag","picoctf","htb")
$ctf = $false
$baseDirectoryPath = "./"


# Transfer OG Termite arguments here
param(
        [Parameter(Mandatory=$false)]
        [string]$path = $baseDirectoryPath,
        [Parameter(Mandatory=$false)]
        [bool]$ctfMode = $ctf
)


function Write-Logo{
    $logo = ("



     ______                     _ __     
    /_  ___|__  _________ ___  (_/ /____ 
     / / / _ \/ ___/ __ `__ \/ / __/ _ \
    / / /  __/ /  / / / / / / / /_/  __/
   /_/  \___/_/  /_/ /_/ /_/_/\__/\___/ 
                                        
                
   
    ")

    Write-Host $logo -ForegroundColor Green

}


function Read-UserParams{
    

}


Write-Logo