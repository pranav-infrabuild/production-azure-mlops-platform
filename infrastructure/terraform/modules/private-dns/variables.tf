variable "private_dns_zone_name" {
  description = "Name of the Azure Private DNS Zone."
  type        = string
}

variable "resource_group_name" {
  description = "Name of the Azure Resource Group."
  type        = string
}

variable "vnet_link_name" {
  description = "Name of the Private DNS Zone Virtual Network Link."
  type        = string
}

variable "virtual_network_id" {
  description = "Resource ID of the Virtual Network to link with the Private DNS Zone."
  type        = string
}

variable "tags" {
  description = "Tags applied to the Private DNS Zone."
  type        = map(string)

  default = {}
}