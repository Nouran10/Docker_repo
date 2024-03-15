# Build Docker image
docker build -t img docker_repo

# Run Docker container
docker run -d --name img-container img
