
terraform {
  backend "azurerm" {
    resource_group_name  = "RGROUP"             ### Must modify, cannot use variable
    storage_account_name = "vmsa1234"           ### Copy storage account name created by bootstrap and paste here
    container_name       = "statefiles"         ### Name of container which contains the tfstate
    key                  = "01.vm.tfstate"      ### Name of storage account which contains the tfstate
  }
}
