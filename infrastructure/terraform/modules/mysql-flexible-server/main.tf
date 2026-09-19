resource "azurerm_mysql_flexible_server" "this" {
  name                = var.server_name
  resource_group_name = var.resource_group_name
  location            = var.location

  administrator_login    = var.administrator_login
  administrator_password = var.administrator_password

  sku_name   = var.sku_name
  version    = var.mysql_version
  storage {
  size_gb           = var.storage_size_gb
  auto_grow_enabled = true
  io_scaling_enabled = true
}

  backup_retention_days = var.backup_retention_days

  geo_redundant_backup_enabled = false

  zone = var.availability_zone

  delegated_subnet_id = var.delegated_subnet_id

  private_dns_zone_id = var.private_dns_zone_id

  public_network_access = "Disabled"

  tags = var.tags
}