provider "aws" {
  region = "us-east-1"
}

module "vpc" {
  source = "./modules/network"
}

module "compute" {
  source = "./modules/compute"
}