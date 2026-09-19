resource "azurerm_key_vault" "this" {
  name                = var.key_vault_name
  location            = var.location
  resource_group_name = var.resource_group_name
  tenant_id            = var.tenant_id

  sku_name = var.sku_name

  public_network_access_enabled = false

  purge_protection_enabled   = true
  soft_delete_retention_days = 90

  rbac_authorization_enabled = true

  tags = var.tags
}