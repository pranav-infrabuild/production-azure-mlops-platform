variable "resource_group_name" {
  description = "Name of the Azure Resource Group."
  type        = string
}

variable "location" {
  description = "Azure region for the resources."
  type        = string
}

variable "storage_account_name" {
  description = "Globally unique ADLS Gen2 storage account name."
  type        = string
}

variable "vnet_name" {
  description = "Name of the Azure Virtual Network."
  type        = string
}

variable "vnet_address_space" {
  description = "CIDR address space of the Virtual Network."
  type        = string
}

variable "subnets" {
  description = "Subnet configuration for the development environment."

  type = map(object({
    address_prefix = string
  }))
}

variable "tags" {
  description = "Tags applied to Azure resources."
  type        = map(string)

  default = {}
}