terraform {
  required_version = ">= 1.6.0"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.0"
    }
  }
}

provider "azurerm" {
  features {}
}

module "adls" {
  source = "../../modules/adls"

  storage_account_name = var.storage_account_name
  resource_group_name  = var.resource_group_name
  location             = var.location
  tags                 = var.tags
}