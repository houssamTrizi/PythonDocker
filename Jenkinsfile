pipeline {
    agent {
        docker {image 'python:3.10.1-alpine'}
        }
    environment {
        HOME = "${env.WORKSPACE}"
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
            steps {
                // 
            }
        }
    }
}
