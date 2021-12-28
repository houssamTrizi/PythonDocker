pipeline {
    agent {
        docker {image 'python:3.10.1-alpine'}
        }
    environment {
        HOME = "${env.WORKSPACE}"
    }
    } 
    stages {
        stage('Build') { 
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') { 
            steps {
                // 
            }
        }
        stage('Deploy') { 
            steps {
                // 
            }
        }
    }
}
