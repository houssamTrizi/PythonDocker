pipeline {
    agent {
        docker {image 'python:3.10.1-alpine'}
        }
    environment {
        HOME = "${env.WORKSPACE}"
        DOCKERHUB_REGISTRY = "houssamtrizi/pythondocker_web:latest"
        DOCKERHUB_CREDENTIALS= "houssamtrizi-dockerhub"
        dockerImage = ''
    } 
    stages {
        stage('Install dependencies') {
            steps {
                sh 'python -m pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python -m pytest tests '
            }
        }
        stage('Deploy') {
            steps{
                script {
                    dockerImage = docker.build DOCKERHUB_REGISTRY
                    docker.withRegistry('', DOCKERHUB_CREDENTIALS){
                        dockerImage.push()
                    }
                }
            }
        }
    }
    post {
        always{
            cleanWs()
        }
    }
}
