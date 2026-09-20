variable "cluster_name" {
  description = "AKS cluster name."
  type        = string
}

variable "location" {
  description = "Azure region."
  type        = string
}

variable "resource_group_name" {
  description = "Resource group name."
  type        = string
}

variable "dns_prefix" {
  description = "DNS prefix for AKS."
  type        = string
}

variable "aks_subnet_id" {
  description = "Subnet ID used by AKS nodes."
  type        = string
}

variable "system_node_vm_size" {
  description = "VM size for the AKS system node pool."
  type        = string
  default     = "Standard_B2s"
}

variable "user_node_vm_size" {
  description = "VM size for the AKS user node pool."
  type        = string
  default     = "Standard_B2s"
}

variable "service_cidr" {
  description = "Kubernetes service CIDR."
  type        = string
  default     = "10.10.0.0/16"
}

variable "dns_service_ip" {
  description = "Kubernetes DNS service IP."
  type        = string
  default     = "10.10.0.10"
}

variable "pod_cidr" {
  description = "Pod CIDR used by AKS overlay networking."
  type        = string
  default     = "10.244.0.0/16"
}

variable "tags" {
  description = "Resource tags."
  type        = map(string)
  default     = {}
}

variable "acr_id" {
  description = "Resource ID of the Azure Container Registry."
  type        = string
}