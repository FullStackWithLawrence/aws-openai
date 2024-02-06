#--------------------------------------------------------------
# Deploy containerized application to an existing Kubernetes cluster
#--------------------------------------------------------------

provider "kubernetes" {
  config_path = "~/.kube/config"
}

# resource "kubernetes_manifest" "deployment" {
#   manifest = yamldecode(data.template_file.deployment.rendered)
# }

# 1. namespace
# 2. service
# 3. horizontal scaling policy
# 4. vertical scaling policy
# 5. certificate
# 6. ingress
# 7. route53 dns record
