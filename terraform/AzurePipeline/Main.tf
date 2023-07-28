// Resource group
data "azurerm_resource_group" "DEK-CI-01-RG" {
  name = "DEK-CI-01-RG"
}

// Create the Linux App Service Plan
resource "azurerm_service_plan" "azplan1" {
  name                = "trungtinplan"
  location            = var.location
  resource_group_name = data.azurerm_resource_group.DEK-CI-01-RG.name
  os_type             = "Linux"
  sku_name            = "B1"
}
// Create the web app, pass in the App Service Plan ID, and deploy code from a public GitHub repo
resource "azurerm_linux_web_app" "webapp1" {
  name                = "trungtinapp"
  location            = var.location
  resource_group_name = data.azurerm_resource_group.DEK-CI-01-RG.name
  service_plan_id = azurerm_service_plan.azplan1.id
  site_config {}
}

## TRUNG TIN

//  Deploy code from a public GitHub repo
//resource "azurerm_app_service_source_control" "sourcecontrol" {
//  app_id   = azurerm_linux_web_app.webapp1.id
//  repo_url = "https://github.com/Azure-Samples/python-docs-hello-world"
//  branch   = "master"
//}

###