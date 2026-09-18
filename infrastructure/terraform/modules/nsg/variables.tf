variable "resource_group_name" {
  description = "Name of the Azure Resource Group."
  type        = string
}

variable "location" {
  description = "Azure region where NSGs will be created."
  type        = string
}

variable "network_security_groups" {
  description = "Map of Network Security Groups to create."
  type        = set(string)
}

variable "network_security_rules" {
  description = "Map of Network Security Rules."

  type = map(object({
    priority                    = number
    direction                   = string
    access                      = string
    protocol                    = string
    source_port_range           = string
    destination_port_range      = string
    source_address_prefix       = string
    destination_address_prefix  = string
    network_security_group_name = string
  }))
}

variable "tags" {
  description = "Tags applied to Network Security Groups."
  type        = map(string)

  default = {}
}

variable "subnet_nsg_associations" {
  description = "Map of subnet names to their associated Network Security Groups."

  type = map(object({
    subnet_id                 = string
    network_security_group_name = string
  }))

  default = {}
}