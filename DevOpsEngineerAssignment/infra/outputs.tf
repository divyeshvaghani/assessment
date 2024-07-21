output "vpc_id" {
  value = module.vpc.vpc_id
}

output "elb_dns_name" {
  value = module.compute.elb_dns_name
}
