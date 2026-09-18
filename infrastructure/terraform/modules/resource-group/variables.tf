variable "resource_group_name" {
  description = "Azure Resource Group Name"
  type        = string
}

variable "location" {
  description = "Azure Region"
  type        = string
}

variable "tags" {
  description = "Tags applied to Resource Group"
  type        = map(string)

  default = {}
}