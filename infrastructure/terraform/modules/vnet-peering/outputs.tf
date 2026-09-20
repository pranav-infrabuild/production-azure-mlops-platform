output "this_to_peer_id" {
  value = azurerm_virtual_network_peering.this_to_peer.id
}

output "peer_to_this_id" {
  value = azurerm_virtual_network_peering.peer_to_this.id
}