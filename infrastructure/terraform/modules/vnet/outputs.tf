output "vnet_id" {
  description = "Resource ID of the Virtual Network."
  value       = azurerm_virtual_network.this.id
}

output "vnet_name" {
  description = "Name of the Virtual Network."
  value       = azurerm_virtual_network.this.name
}

output "subnet_ids" {
  description = "Map of subnet names to subnet resource IDs."
  value = {
    for name, subnet in azurerm_subnet.this :
    name => subnet.id
  }
}

output "subnet_names" {
  description = "List of created subnet names."
  value       = keys(azurerm_subnet.this)
}