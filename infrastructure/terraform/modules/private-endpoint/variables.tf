variable "private_endpoint_name" {
  description = "Name of the Azure Private Endpoint."
  type        = string
}

variable "private_service_connection_name" {
  description = "Name of the Private Service Connection."
  type        = string
}

variable "private_connection_resource_id" {
  description = "Resource ID of the Azure service to connect privately."
  type        = string
}

variable "subresource_names" {
  description = "Subresource names exposed by the target Azure service."
  type        = list(string)
}

variable "subnet_id" {
  description = "Resource ID of the subnet where the Private Endpoint will be deployed."
  type        = string
}

variable "resource_group_name" {
  description = "Name of the Azure Resource Group."
  type        = string
}

variable "location" {
  description = "Azure region where the Private Endpoint will be created."
  type        = string
}

variable "tags" {
  description = "Tags applied to the Private Endpoint."
  type        = map(string)

  default = {}
}

variable "private_dns_zone_group_name" {
  description = "Name of the Private DNS Zone Group."
  type        = string
}

variable "private_dns_zone_ids" {
  description = "IDs of Private DNS Zones associated with the Private Endpoint."
  type        = list(string)
}