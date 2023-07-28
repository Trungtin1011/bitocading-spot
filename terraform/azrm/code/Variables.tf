# Everytime a variable is created in the file "Terraform.tfvar", must define that variable here

// Main
variable "tenant_id" {
  type        = string
  default     = ""
  description = "indicate the ID of Azure tenant (Azure context)"
}

variable "subscription_id" {
  type        = string
  default     = ""
  description = "indicate the ID of subscription (Azure context)"
}

variable "azure_region" {
  type        = string
  default     = ""
  description = "define the azure region where the resource is deployed (Azure convention)"
}

variable "rg_name" {
  type        = string
  default     = ""
  description = ""
}


// Tagging
variable "tag_entity" {
  type        = string
  default     = ""
  description = "define the name of the entity (LVMH trigram)"
}

variable "tag_environment" {
  type        = string
  default     = ""
  description = "define the environment"
}

variable "tag_index" {
  type        = string
  default     = ""
  description = "define the index of the resource"
}

variable "tag_location" {
  type        = string
  default     = ""
  description = "define the azure region where the resource is deployed (LVMH code)"
}

variable "tag_project" {
  type        = string
  default     = ""
  description = "define the name of the project"
}

variable "tag_cost_center" {
  type        = string
  default     = ""
  description = ""
}

variable "tag_deployment_method" {
  type        = string
  default     = ""
  description = ""
}

variable "tag_msp" {
  type        = string
  default     = ""
  description = ""
}

variable "tag_owner" {
  type        = string
  default     = ""
  description = ""
}

variable "tag_role" {
  type        = string
  default     = ""
  description = ""
}

