variable "location" {
  type				= string
  description	= "Azure Region for resources. Defaults to Japan East."
  default			= "Southeast Asia"
}
variable "tags" {
  type    = map(string)
  default = {
    CreationDate = "2023-xx-xx"
    Owner = "TrungTin"
    Aim = "LearnAzure"
    ModifyWith = "Terraform"
  }
}