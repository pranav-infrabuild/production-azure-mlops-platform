terraform {
  required_version = ">=1.6.0"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>4.0"
    }
  }
}

provider "azurerm" {
  features {}
}

module "resource_group" {
  source = "../../modules/resource-group"

  resource_group_name = var.resource_group_name
  location            = var.location
  tags                = var.tags
}

module "adls" {
  source = "../../modules/adls"

  storage_account_name = var.storage_account_name
  resource_group_name  = module.resource_group.resource_group_name
  location             = module.resource_group.location
  tags                 = var.tags

  depends_on = [
    module.resource_group
  ]
}