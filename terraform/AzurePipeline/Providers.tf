# We strongly recommend using the required_providers block to set the
# Azure Provider source and version being used
terraform {
  required_version = ">= 1.0.0"
  required_providers {
    azurerm = "~> 3.0.0"
  }
}

provider "azurerm" {  
  subscription_id = "c22125fc-43c7-4b74-b86c-a66704880310"
  features {}
}
