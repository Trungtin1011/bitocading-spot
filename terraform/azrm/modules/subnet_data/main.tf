
data "azurerm_subnet" "Subnet" {
    
    // references: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/data-sources/subnet

    resource_group_name  = var.resource_group_name

    name                 = var.subnet_name
    virtual_network_name = var.virtual_network_name
  
}
