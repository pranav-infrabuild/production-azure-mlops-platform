resource "azurerm_user_assigned_identity" "this" {
  name                = var.identity_name
  resource_group_name = var.resource_group_name
  location            = var.location

  tags = var.tags
}
resource "azurerm_role_assignment" "key_vault_secrets_user" {
  scope                = var.key_vault_id
  role_definition_name = "Key Vault Secrets User"
  principal_id         = azurerm_user_assigned_identity.this.principal_id
}

resource "azurerm_federated_identity_credential" "aks" {
  name                = "fic-aks-mlops-dev"
  resource_group_name = var.resource_group_name
  parent_id           = azurerm_user_assigned_identity.this.id

  audience = [
    "api://AzureADTokenExchange"
  ]

  issuer = var.oidc_issuer_url

  subject = "system:serviceaccount:mlops:mlops-workload"
}