variable "vnet_name" {
  description = "Name of the Azure Virtual Network."
  type        = string
}

variable "vnet_address_space" {
  description = "CIDR address space of the Virtual Network."
  type        = string
}

variable "resource_group_name" {
  description = "Name of the Azure Resource Group."
  type        = string
}

variable "location" {
  description = "Azure region where the VNet will be created."
  type        = string
}

variable "subnets" {
  description = "Map of subnet names and their CIDR address prefixes."

  type = map(object({
    address_prefix = string

    delegation = optional(object({
      name         = string
      service_name = string
      actions      = list(string)
    }))
  }))
}

variable "tags" {
  description = "Tags applied to the Virtual Network."
  type        = map(string)

  default = {}
}