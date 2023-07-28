// Resource group
module "ResourceGroup" {
  source = "../modules/resource_group_data"
  resource_group_name = "LEP-WLX-PRD-01-RGROUP"   ### Need to check
}

// Subnet
module "Subnet" {
  source = "../modules/subnet_data"
  subnet_name           = "INTRANET-01-SUBNET"        ### Need to check
  virtual_network_name  = "AFRC-LEP-WLX-PRD-01-VNET"  ### Need to check
  resource_group_name   = "LEP-WLX-PRD-01-RGROUP"     ### RG of the vnet above
}

// Virtual machine windows
module "AZURE_VM" {
  source = "../modules/virtual_machine_windows_2019"  ### Need to check for the folder name

  // resource group
  resource_group_name     = module.ResourceGroup.resource_group_name
  resource_group_location = module.ResourceGroup.resource_group_location

  // image    ### Need to check carefully to fill all the information needed
  admin_username                  = "adminroot"
  admin_password                  = random_password.password.result
  virtual_machine_name            = "AZLEPICBKPRD01"
  virtual_machine_size            = "Standard_A2_v2"
  sku_type                        = "2019-Datacenter-gensecond"
  os_disk_name                    = "AZLEPICBKPRD01-OS-01-DISK"
  os_disk_type                    = "Premium_LRS"
  virtual_machine_nic_name        = "AZLEPICBKPRD01-01-NIC"
  virtual_machine_nic_ip_address  = "10.70.217.152"
  virtual_machine_nic_subnet_id   = module.Subnet.subnet_id
  availability_zone               = "2"

  // storage account
  storage_account_name = "azlepicbkprd01diagsa"    ### Check for naming convention: VM name + diagsa

  // tag
  tag_application       = "icebreaker" ### Name of the VM in lowercase
  tag_cost_center       = var.tag_cost_center
  tag_deployment_method = var.tag_deployment_method
  tag_entity            = var.tag_entity
  tag_environment       = var.tag_environment
  tag_location          = var.tag_location
  tag_msp               = var.tag_msp
  tag_owner             = var.tag_owner 
  tag_role              = var.tag_role 

  depends_on = [
    module.ResourceGroup,
    module.Subnet
  ]
  
}

### Build data disk ###
resource "azurerm_managed_disk" "data_disk_vm" {

// resource group
  location             = module.ResourceGroup.resource_group_location
  resource_group_name  = module.ResourceGroup.resource_group_name

// disk properties
  name                 = "VM-DATA-01-DISK"  ### Need to check
  storage_account_type = "Premium_LRS"      ### Standard_LRS / StandardSSD_LRS / Premium_LRS
  zones                = ["1"]              ### Need to check
  create_option        = "Empty"
  disk_size_gb         = 60                 ### Need to check

//tags
    tags = {
    Application       = ""          ### Need to check
    Cost_center       = var.tag_cost_center
    Deployment_method = var.tag_deployment_method
    Entity            = var.tag_entity
    Environment       = var.tag_environment
    Location          = var.tag_location
    Owner             = var.tag_owner
    Msp               = var.tag_msp
    Role              = "data_disk" ### Need to check

  }

}

### Attach data disk to VM ### 
resource "azurerm_virtual_machine_data_disk_attachment" "diskassociate_vm" {

  managed_disk_id    = azurerm_managed_disk.data_disk_vm.id  ### Need to check
  virtual_machine_id = module.AZURE_VM.virtual_machine_id                 ### Need to check
  lun                = "0"
  caching            = "ReadWrite"

  depends_on = [
    module.AZURE_VM  ### Need to check
  ]
  
}
