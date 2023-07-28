## Import Resource Group Before Apply ##

# Note: For existing resource group, must import first with command:
# terraform import azurerm_resource_group.RESOURCE_GROUP_NAME /subscriptions/SUBSCRIPTION_ID/resourceGroups/RESOURCE_GROUP_NAME

resource "azurerm_resource_group" "aksrg" {
  name     = "RESOURCE_GROUP_NAME"
  location = "RESOURCE_GROUP_LOCATION"

  tags = {
    environment = "Demo"
  }
}

resource "azurerm_kubernetes_cluster" "akscluster" {
  name                = "CLUSTER_NAME"
  location            = azurerm_resource_group.aksrg.location
  resource_group_name = azurerm_resource_group.aksrg.name
  dns_prefix          = "demo-k8s"

  default_node_pool {
    name            = "aksdemo"
    node_count      = 2
    vm_size         = "Standard_B2s"
    os_disk_size_gb = 30
  }

  service_principal {
    client_id     = var.appId
    client_secret = var.password
  }

  # role_based_access_control {
  #   enabled = true
  # }
  # Since v3.58.0, azurerm change the block to role_based_access_control_enabled (default = true)
  role_based_access_control_enabled = true

  tags = {
    environment = "Demo"
  }
}
