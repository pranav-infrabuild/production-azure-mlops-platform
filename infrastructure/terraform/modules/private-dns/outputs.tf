output "private_dns_zone_id" {
  description = "Resource ID of the Azure Private DNS Zone."
  value       = azurerm_private_dns_zone.this.id
}

output "private_dns_zone_name" {
  description = "Name of the Azure Private DNS Zone."
  value       = azurerm_private_dns_zone.this.name
}