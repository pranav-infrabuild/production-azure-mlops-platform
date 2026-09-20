resource "azurerm_virtual_network_peering" "this_to_peer" {
  name                      = var.this_to_peer_name
  resource_group_name       = var.resource_group_name
  virtual_network_name      = var.this_vnet_name
  remote_virtual_network_id = var.remote_vnet_id

  allow_virtual_network_access = true
  allow_forwarded_traffic      = true
}

resource "azurerm_virtual_network_peering" "peer_to_this" {
  name                      = var.peer_to_this_name
  resource_group_name       = var.remote_resource_group_name
  virtual_network_name      = var.remote_vnet_name
  remote_virtual_network_id = var.this_vnet_id

  allow_virtual_network_access = true
  allow_forwarded_traffic      = true
}