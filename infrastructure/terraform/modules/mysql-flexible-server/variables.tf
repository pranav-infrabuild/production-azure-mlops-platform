variable "server_name" {
  description = "Name of the MySQL Flexible Server."
  type        = string
}

variable "resource_group_name" {
  description = "Name of the Azure Resource Group."
  type        = string
}

variable "location" {
  description = "Azure region where the MySQL server will be deployed."
  type        = string
}

variable "administrator_login" {
  description = "Administrator username for MySQL."
  type        = string
}

variable "administrator_password" {
  description = "Administrator password for MySQL."
  type        = string
  sensitive   = true
}

variable "sku_name" {
  description = "SKU name for the MySQL Flexible Server."
  type        = string
  default     = "B_Standard_B1ms"
}

variable "mysql_version" {
  description = "MySQL major version."
  type        = string
  default     = "8.0.21"
}

variable "storage_size_gb" {
  description = "Storage size of the MySQL Flexible Server in GiB."
  type        = number
  default     = 32
}

variable "backup_retention_days" {
  description = "Number of days to retain backups."
  type        = number
  default     = 7
}

variable "availability_zone" {
  description = "Availability zone for the MySQL server."
  type        = string
  default     = "1"
}

variable "delegated_subnet_id" {
  description = "Resource ID of the delegated database subnet."
  type        = string
}

variable "private_dns_zone_id" {
  description = "Resource ID of the private DNS zone for MySQL."
  type        = string
}

variable "tags" {
  description = "Tags applied to the MySQL server."
  type        = map(string)
  default     = {}
}