resource "random_password" "password" {

  length  = 30
  lower   = true
  upper   = true
  number  = true
  special = false

}


output "AdminPassword" {
    value = random_password.password.result
    sensitive = true
  
}