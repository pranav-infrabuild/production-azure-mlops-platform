output "network_security_group_ids" {
  description = "Map of Network Security Group names to resource IDs."
  value = {
    for name, nsg in azurerm_network_security_group.this :
    name => nsg.id
  }
}

output "network_security_group_names" {
  description = "List of created Network Security Group names."
  value       = keys(azurerm_network_security_group.this)
}