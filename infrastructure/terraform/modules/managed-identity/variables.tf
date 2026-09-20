variable "identity_name" {
  type = string
}

variable "resource_group_name" {
  type = string
}

variable "location" {
  type = string
}

variable "tags" {
  type    = map(string)
  default = {}
}
variable "key_vault_id" {
  type = string
}

variable "oidc_issuer_url" {
  type = string
}
