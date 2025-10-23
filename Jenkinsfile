pipeline {
    agent any
    environment {
        IMAGE_NAME = "my-django-app:${env.BUILD_NUMBER}"
        CONTAINER_NAME = "django-app"
    }
    stages {
        stage('Lint Code') {
            steps {
                echo "Running linter (flake8)..."
                sh "flake8 ."
            }
        }
        stage('Run Unit Tests') {
            steps {
                echo "Running Django unit tests..."
                sh "python manage.py test"
            }
        }
        stage('Build Docker Image') {
            steps {
                echo "Building the Docker image: ${IMAGE_NAME}"
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Stop & Remove Old Container') {
            steps {
                echo "Stopping and removing any old container..."
                sh "docker stop ${CONTAINER_NAME} || true"
                sh "docker rm ${CONTAINER_NAME} || true"
            }
        }

        stage('Run New Container') {
            steps {
                echo "Running the new container on port 80..."
                sh "docker run -d --name ${CONTAINER_NAME} -p 80:8000 ${IMAGE_NAME}"
            }
        }

    post {
        success {
            echo "Pipeline successful! App is deployed."
            sh "docker image prune -f"
        }
        failure {
            echo "Pipeline failed!"
        }
    }
}