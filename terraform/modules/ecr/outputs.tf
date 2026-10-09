output "repository_url" {
  description = "URL ECR repository"
  value       = aws_ecr_repository.app.repository_url
}

output "repository_name" {
  description = "Nazev ECR repository"
  value       = aws_ecr_repository.app.name
}