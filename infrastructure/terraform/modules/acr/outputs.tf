output "registry_id" {
  description = "Resource ID of the Azure Container Registry."
  value       = azurerm_container_registry.this.id
}

output "registry_name" {
  description = "Name of the Azure Container Registry."
  value       = azurerm_container_registry.this.name
}

output "login_server" {
  description = "ACR login server."
  value       = azurerm_container_registry.this.login_server
}

output "resource_group_name" {
  description = "Resource group containing the ACR."
  value       = azurerm_container_registry.this.resource_group_name
}