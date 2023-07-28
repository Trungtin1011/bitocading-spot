# We strongly recommend using the required_providers block to set the
# Azure Provider source and version being used
terraform {
  required_version = ">= 1.0.0"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0.0"
    }
  }
}


provider "azurerm" {
  features {}
  skip_provider_registration = true
}