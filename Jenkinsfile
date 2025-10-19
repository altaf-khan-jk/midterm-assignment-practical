pipeline {
  agent any
  environment {
    // For Docker push via credentials in Jenkins (set up separately)
    DOCKER_REGISTRY = 'docker.io'
    IMAGE_NAME = "ci-sample-python"
    // CREDENTIALS_ID should be replaced with the ID you set in Jenkins (Docker Hub credentials)
    CREDENTIALS_ID = 'dockerhub-credentials'
  }
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Install Dependencies') {
      steps {
        sh 'python -m venv .venv || true'
        sh '. .venv/bin/activate && pip install --upgrade pip && pip install -r app/requirements.txt pytest'
      }
    }
    stage('Test') {
      steps {
        sh '. .venv/bin/activate && pytest -q'
      }
    }
    stage('Build Docker Image') {
      steps {
        script {
          dockerImage = docker.build("${env.IMAGE_NAME}:latest")
        }
      }
    }
    stage('Push Docker Image') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'ghcr-token', usernameVariable: 'USERNAME', passwordVariable: 'TOKEN')]) {
            sh 'echo $TOKEN | docker login ghcr.io -u $USERNAME --password-stdin'
            sh "docker push ${IMAGE_NAME}:${BUILD_NUMBER}"
            sh "docker push ${IMAGE_NAME}:latest"
        }
      }
    }
  }
}
