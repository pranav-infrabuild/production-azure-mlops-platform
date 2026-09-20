resource "azurerm_data_factory_custom_dataset" "adls_processed" {
  name            = "ds-adls-processed"
  data_factory_id = azurerm_data_factory.this.id
  type            = "Parquet"

  linked_service {
    name = azurerm_data_factory_linked_service_data_lake_storage_gen2.adls.name
  }

  type_properties_json = jsonencode({
    location = {
      type       = "AzureBlobFSLocation"
      folderPath = "processed"
    }
  })
}