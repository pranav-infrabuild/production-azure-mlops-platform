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

    delegation = optional(object({
      name         = string
      service_name = string
      actions      = list(string)
    }))
  }))
}

variable "tags" {
  description = "Tags applied to Azure resources."
  type        = map(string)

  default = {}
}

variable "mysql_server_name" {
  description = "Name of the MySQL Flexible Server."
  type        = string
}

variable "mysql_administrator_login" {
  description = "Administrator username for MySQL."
  type        = string
}

variable "mysql_administrator_password" {
  description = "Administrator password for MySQL."
  type        = string
  sensitive   = true
}

variable "mysql_sku_name" {
  description = "SKU name for the MySQL Flexible Server."
  type        = string
  default     = "B_Standard_B1ms"
}

variable "mysql_version" {
  description = "MySQL major version."
  type        = string
  default     = "8.0.21"
}

variable "mysql_storage_size_gb" {
  description = "Storage size of the MySQL server in GiB."
  type        = number
  default     = 32
}

variable "mysql_backup_retention_days" {
  description = "Number of days to retain MySQL backups."
  type        = number
  default     = 7
}

variable "mysql_availability_zone" {
  description = "Availability zone for the MySQL server."
  type        = string
  default     = "1"
}
variable "acr_name" {
  description = "Globally unique Azure Container Registry name."
  type        = string
}

variable "acr_sku" {
  description = "Azure Container Registry SKU."
  type        = string
  default     = "Premium"

  validation {
    condition     = contains(["Basic", "Standard", "Premium"], var.acr_sku)
    error_message = "ACR SKU must be Basic, Standard, or Premium."
  }
}
variable "key_vault_name" {
  description = "Globally unique Azure Key Vault name."
  type        = string
}

variable "key_vault_sku" {
  description = "Azure Key Vault SKU."
  type        = string
  default     = "standard"

  validation {
    condition     = contains(["standard", "premium"], var.key_vault_sku)
    error_message = "Key Vault SKU must be standard or premium."
  }
}
variable "managed_identity_name" {
  type    = string
  default = "id-mlops-dev"
}
