terraform {
  backend "azurerm" {
    resource_group_name  = "DEK-CI-01-RG"  ### Must modify, cannot use variable
    storage_account_name = "tfsaving"     
    container_name       = "tfstate"            
    key                  = "key.tfstate.01"  
  }
}
