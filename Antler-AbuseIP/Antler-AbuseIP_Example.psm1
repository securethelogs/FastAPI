function Get-AntlerIP {
    param(
        [string] $IP,
        [string] $List
        )

    
    if (!$List){

        (Invoke-RestMethod "https://<Your_HOST>/abuse/$($IP)").Data

    } else {

        if ($List.toUpper().EndsWith(".TXT")){

            if (Test-Path $List){

                $IPs = @(Get-Content $List)
                $Results = @()

                foreach ($I in $IPs){

                  (Invoke-RestMethod "https://<Your_HOST>/abuse/$($I)").Data


                }
             

            } else { Write-Host "[!] Error: Path not valid" -ForegroundColor Red}


        } else { Write-Host "[!] Error: Please submit a TXT file" -ForegroundColor Red }
    

    }



}
