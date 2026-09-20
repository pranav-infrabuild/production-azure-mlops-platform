output "storage_account_id" {
  description = "Resource ID of the ADLS Gen2 storage account."
  value       = module.adls.storage_account_id
}

output "storage_account_name" {
  description = "Name of the ADLS Gen2 storage account."
  value       = module.adls.storage_account_name
}

output "primary_dfs_endpoint" {
  description = "Primary DFS endpoint of the ADLS Gen2 storage account."
  value       = module.adls.primary_dfs_endpoint
}

output "managed_identity_client_id" {
  value = module.managed_identity.client_id
}

output "managed_identity_principal_id" {
  value = module.managed_identity.principal_id
}