variable "storage_account_name" {
  description = "Globally unique ADLS Gen2 storage account name."
  type        = string
}

variable "resource_group_name" {
  description = "Name of the Azure resource group."
  type        = string
}

variable "location" {
  description = "Azure region for the resources."
  type        = string
}

variable "tags" {
  description = "Tags applied to Azure resources."
  type        = map(string)
  default     = {}
}