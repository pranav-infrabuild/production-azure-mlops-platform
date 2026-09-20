resource "azurerm_data_factory_linked_service_data_lake_storage_gen2" "adls" {
  name            = "ls-adls-gen2"
  data_factory_id = azurerm_data_factory.this.id
  url             = "https://stmlopsdev925714.dfs.core.windows.net"

  use_managed_identity = true
}