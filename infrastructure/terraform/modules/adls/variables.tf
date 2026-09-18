variable "storage_account_name" {
  description = "Globally unique name of the ADLS Gen2 storage account."
  type        = string

  validation {
    condition = (
      length(var.storage_account_name) >= 3 &&
      length(var.storage_account_name) <= 24 &&
      can(regex("^[a-z0-9]+$", var.storage_account_name))
    )

    error_message = "Storage account name must be 3-24 characters and contain only lowercase letters and numbers."
  }
}

variable "resource_group_name" {
  description = "Name of the Azure resource group."
  type        = string
}

variable "location" {
  description = "Azure region where the storage account will be created."
  type        = string
}

variable "tags" {
  description = "Tags to apply to the storage account."
  type        = map(string)
  default     = {}
}