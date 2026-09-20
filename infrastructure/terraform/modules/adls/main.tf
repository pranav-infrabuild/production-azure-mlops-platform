resource "azurerm_storage_account" "this" {
  name                     = var.storage_account_name
  resource_group_name      = var.resource_group_name
  location                 = var.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  is_hns_enabled = true

  min_tls_version = "TLS1_2"

  public_network_access_enabled = false

  allow_nested_items_to_be_public = false

  shared_access_key_enabled = false

  default_to_oauth_authentication = true

  local_user_enabled = false

  tags = var.tags
}
