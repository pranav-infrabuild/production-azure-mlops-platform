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
  resource_provider_registrations = "none"
  storage_use_azuread             = true
}
data "azurerm_client_config" "current" {}
module "resource_group" {
  source = "../../modules/resource-group"

  resource_group_name = var.resource_group_name
  location            = var.location
  tags                = var.tags
}

module "acr" {
  source = "../../modules/acr"

  registry_name       = var.acr_name
  resource_group_name = module.resource_group.resource_group_name
  location            = var.location

  sku = var.acr_sku

  tags = var.tags
}
module "vnet" {
  source = "../../modules/vnet"

  vnet_name           = var.vnet_name
  vnet_address_space  = var.vnet_address_space
  resource_group_name = module.resource_group.resource_group_name
  location            = module.resource_group.location
  subnets             = var.subnets
  tags                = var.tags

  depends_on = [
    module.resource_group
  ]
}

module "mysql_vnet" {
  source = "../../modules/vnet"

  vnet_name          = "vnet-mysql-eastasia"
  vnet_address_space = "172.18.0.0/16"

  resource_group_name = module.resource_group.resource_group_name
  location            = "East Asia"

  subnets = {
    database-subnet = {
      address_prefix = "172.18.1.0/24"

      delegation = {
        name         = "mysql-flexible-server-delegation"
        service_name = "Microsoft.DBforMySQL/flexibleServers"
        actions = [
          "Microsoft.Network/virtualNetworks/subnets/join/action"
        ]
      }
    }
  }

  tags = var.tags
}
module "nsg" {
  source = "../../modules/nsg"

  resource_group_name = module.resource_group.resource_group_name
  location            = module.resource_group.location

  network_security_groups = [
    "nsg-aks-dev",
    "nsg-management-dev",
    "nsg-database-dev",
    "nsg-private-endpoint-dev"
  ]

  network_security_rules = {
    allow-https-inbound = {
      priority                    = 100
      direction                   = "Inbound"
      access                      = "Allow"
      protocol                    = "Tcp"
      source_port_range           = "*"
      destination_port_range      = "443"
      source_address_prefix       = "*"
      destination_address_prefix  = "*"
      network_security_group_name = "nsg-aks-dev"
    }

    allow-http-inbound = {
      priority                    = 110
      direction                   = "Inbound"
      access                      = "Allow"
      protocol                    = "Tcp"
      source_port_range           = "*"
      destination_port_range      = "80"
      source_address_prefix       = "*"
      destination_address_prefix  = "*"
      network_security_group_name = "nsg-aks-dev"
    }
  }

  subnet_nsg_associations = {
    aks-subnet = {
      subnet_id                   = module.vnet.subnet_ids["aks-subnet"]
      network_security_group_name = "nsg-aks-dev"
    }

    management-subnet = {
      subnet_id                   = module.vnet.subnet_ids["management-subnet"]
      network_security_group_name = "nsg-management-dev"
    }

    database-subnet = {
      subnet_id                   = module.vnet.subnet_ids["database-subnet"]
      network_security_group_name = "nsg-database-dev"
    }

    private-endpoint-subnet = {
      subnet_id                   = module.vnet.subnet_ids["private-endpoint-subnet"]
      network_security_group_name = "nsg-private-endpoint-dev"
    }
  }

  tags = var.tags

  depends_on = [
    module.resource_group
  ]
}

module "adls_private_endpoint" {
  source = "../../modules/private-endpoint"

  private_endpoint_name = "pe-adls-dev"

  private_service_connection_name = "psc-adls-dev"

  private_connection_resource_id = module.adls.storage_account_id

  subresource_names = [
    "dfs"
  ]

  subnet_id = module.vnet.subnet_ids["private-endpoint-subnet"]

  private_dns_zone_group_name = "default"

  private_dns_zone_ids = [
    module.adls_private_dns.private_dns_zone_id
  ]

  resource_group_name = module.resource_group.resource_group_name
  location            = module.resource_group.location

  tags = var.tags

  depends_on = [
    module.adls,
    module.vnet,
    module.adls_private_dns
  ]
}

module "adls_private_dns" {
  source = "../../modules/private-dns"

  private_dns_zone_name = "privatelink.dfs.core.windows.net"

  resource_group_name = module.resource_group.resource_group_name

  vnet_link_name = "link-adls-dfs-dev"

  virtual_network_id = module.vnet.vnet_id

  tags = var.tags

  depends_on = [
    module.vnet
  ]
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

module "mysql" {
  source = "../../modules/mysql-flexible-server"

  server_name = var.mysql_server_name

  resource_group_name = module.resource_group.resource_group_name
  location            = "East Asia"

  administrator_login    = var.mysql_administrator_login
  administrator_password = var.mysql_administrator_password

  sku_name        = var.mysql_sku_name
  mysql_version   = var.mysql_version
  storage_size_gb = var.mysql_storage_size_gb

  backup_retention_days = var.mysql_backup_retention_days

  availability_zone = var.mysql_availability_zone

  delegated_subnet_id = module.mysql_vnet.subnet_ids["database-subnet"]

  private_dns_zone_id = module.mysql_private_dns.private_dns_zone_id

  tags = var.tags

  depends_on = [
    module.vnet,
    module.mysql_private_dns
  ]
}
module "mysql_private_dns" {
  source = "../../modules/private-dns"

  private_dns_zone_name = "privatelink.mysql.database.azure.com"

  resource_group_name = module.resource_group.resource_group_name

  vnet_link_name = "link-mysql-dev"

  virtual_network_id = module.vnet.vnet_id

  tags = var.tags

  depends_on = [
    module.vnet
  ]
}

resource "azurerm_private_dns_zone_virtual_network_link" "mysql_eastasia" {
  name                  = "link-mysql-eastasia"
  resource_group_name   = module.resource_group.resource_group_name
  private_dns_zone_name = "privatelink.mysql.database.azure.com"
  virtual_network_id    = module.mysql_vnet.vnet_id

  registration_enabled = false

  tags = var.tags

  depends_on = [
    module.mysql_private_dns,
    module.mysql_vnet
  ]
}
module "acr_private_dns" {
  source = "../../modules/private-dns"

  private_dns_zone_name = "privatelink.azurecr.io"

  resource_group_name = module.resource_group.resource_group_name

  vnet_link_name = "link-acr-dev"

  virtual_network_id = module.vnet.vnet_id

  tags = var.tags

  depends_on = [
    module.vnet
  ]
}

module "acr_private_endpoint" {
  source = "../../modules/private-endpoint"

  private_endpoint_name = "pe-acr-dev"

  private_service_connection_name = "psc-acr-dev"

  private_connection_resource_id = module.acr.registry_id

  subresource_names = [
    "registry"
  ]

  subnet_id = module.vnet.subnet_ids["private-endpoint-subnet"]

  resource_group_name = module.resource_group.resource_group_name

  location = var.location

  private_dns_zone_group_name = "acr-dns-zone-group"

  private_dns_zone_ids = [
    module.acr_private_dns.private_dns_zone_id
  ]

  tags = var.tags

  depends_on = [
    module.acr,
    module.acr_private_dns
  ]
}

module "key_vault" {
  source = "../../modules/key-vault"

  key_vault_name      = var.key_vault_name
  resource_group_name = module.resource_group.resource_group_name
  location            = var.location

  tenant_id = data.azurerm_client_config.current.tenant_id

  sku_name = var.key_vault_sku

  tags = var.tags

  depends_on = [
    module.resource_group
  ]
}

module "key_vault_private_dns" {
  source = "../../modules/private-dns"

  private_dns_zone_name = "privatelink.vaultcore.azure.net"

  resource_group_name = module.resource_group.resource_group_name

  vnet_link_name = "link-key-vault-dev"

  virtual_network_id = module.vnet.vnet_id

  tags = var.tags

  depends_on = [
    module.vnet
  ]
}

module "key_vault_private_endpoint" {
  source = "../../modules/private-endpoint"

  private_endpoint_name = "pe-key-vault-dev"

  private_service_connection_name = "psc-key-vault-dev"

  private_connection_resource_id = module.key_vault.key_vault_id

  subresource_names = [
    "vault"
  ]

  subnet_id = module.vnet.subnet_ids["private-endpoint-subnet"]

  resource_group_name = module.resource_group.resource_group_name

  location = var.location

  private_dns_zone_group_name = "key-vault-dns-zone-group"

  private_dns_zone_ids = [
    module.key_vault_private_dns.private_dns_zone_id
  ]

  tags = var.tags

  depends_on = [
    module.key_vault,
    module.key_vault_private_dns
  ]
}