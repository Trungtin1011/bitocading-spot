
##### FUNCTIONS #####
function Init {

    Clear-Host

    $Credential = Get-Credential    ### Credential of the SPN used to create resources

    $TenantId               = ""                        ### Need to check
    $SubscriptionId         = ""                        ### Need to check
    $ResourceGroupName      = "RGROUP"                  ### Need to check
    $Location               = ""                        ### Need to check
    $StorageAccountName     = "vmsa"                    ### Name of storage account which contains the tfstate  
    $StorageAccountSku      = "Standard_GRS"            ### Remain the same
    $StorageAccountKind     = "StorageV2"               ### Remain the same
    $StorageContainerName   = "statefiles"              ### Remain the same

    Connect-AzAccount -ServicePrincipal -TenantId $TenantId -Credential $Credential

    Set-AzContext -SubscriptionId $SubscriptionId 
    
    Get-AzContext

    GenerateString

}

function GenerateString {

    $Number = Get-Random -Maximum 9999
    
    $StorageAccountName = $StorageAccountName + $Number
    Write-Host "[info] Storage Account name has been identified: $StorageAccountName "
    
    CheckResourceGroup

}

function CheckResourceGroup {

    $ResourceGroup = Get-AzResourceGroup -ResourceGroupName $ResourceGroupName -ErrorAction SilentlyContinue
    
    if($ResourceGroup) {
    
        Write-Host "[info] Resource Group has been found. "
    
        CheckStorageAccount
    
    }
    else {
    
        Write-Host "[info] Resource Group has not been found. "
        Write-Host " "
    
        $CreateResourceGroup = Read-Host "[question] Do you want to create Resource Group? (yes/no)"
    
        if($CreateResourceGroup -eq "yes"){

            New-AzResourceGroup -ResourceGroupName $ResourceGroupName -Location $Location | Out-Null
            Write-Host " "
            Write-Host "[info] Resource Group has been created. "

            CheckStorageAccount

        }
        else {
    
            Write-Host "[info] Resource Group is not created (user choice). "

            Return
    
        }
    }
}

function CheckStorageAccount {

    $StorageAccount = Get-AzStorageAccount -Name $StorageAccountName -ResourceGroupName $ResourceGroupName -ErrorAction SilentlyContinue
    
    if($StorageAccount) {
    
        Write-Host "[info] Storage Account has been found with name $StorageAccountName "
    
        $StorageAccountKey = (Get-AzStorageAccountKey -ResourceGroupName $ResourceGroupName -AccountName $StorageAccountName)| Where-Object {$_.KeyName -eq "key1"} -ErrorAction SilentlyContinue
    
        if($StorageAccountKey) {
    
            Write-Host "[info] Storage Account Key has been found. "

            $StorageAccountKey = $StorageAccountKey.Value
            
            $StorageContext = New-AzStorageContext -StorageAccountName $StorageAccountName -StorageAccountKey $StorageAccountKey -ErrorAction SilentlyContinue
    
            if($StorageContext) {
            
                Write-Host "[info] Storage Context has been set. "

                $StorageContainer = Get-AzStorageContainer -Name $StorageContainerName -Context $StorageContext -ErrorAction SilentlyContinue

                if($StorageContainer) {

                    Write-Host "[info] Storage Container has been found. "
                    Write-Host "[info] Bootstrap has been set. "

                    Return

                }
                else {
                    
                    CreateStorageContainer
    
                }
                            
            }
            else {
            
                Write-Host "[error] Storage Context has not been set. "
            
            }
        }
        else {

            Write-Host "[error] Storage Account Key has not been found. "

        }

    }
    else {
    
        Write-Host "[info] Storage Account has not been found. "
        Write-Host "[info] Storage Account can be created with name: $StorageAccountName "
        Write-Host "[info] next step: creation of Storage Account. "

        CreateStorageAccount

    }    
}

function CreateStorageAccount {

    New-AzStorageAccount -ResourceGroupName $ResourceGroupName -Name $StorageAccountName -Location $Location -SkuName $StorageAccountSku | Out-Null
    
    CheckStorageAccount

}

function CreateStorageContainer {

    New-AzStorageContainer -Name $StorageContainerName -Context $StorageContext -Permission Off | Out-Null
    
    CheckStorageAccount

}



##### INIT #####
Init
