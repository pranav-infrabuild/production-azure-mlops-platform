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