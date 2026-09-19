variable "registry_name" {
  description = "Globally unique Azure Container Registry name."
  type        = string
}

variable "resource_group_name" {
  description = "Resource group where the ACR will be deployed."
  type        = string
}

variable "location" {
  description = "Azure region for the ACR."
  type        = string
}

variable "sku" {
  description = "ACR SKU. Premium is required for Private Link."
  type        = string
  default     = "Premium"

  validation {
    condition     = contains(["Basic", "Standard", "Premium"], var.sku)
    error_message = "SKU must be Basic, Standard, or Premium."
  }
}

variable "tags" {
  description = "Tags applied to the ACR."
  type        = map(string)
  default     = {}
}