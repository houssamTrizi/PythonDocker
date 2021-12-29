pipeline {
    agent {
        docker {image 'python:3.10.1-alpine'}
        }
    environment {
        HOME = "${env.WORKSPACE}"
        DOCKERHUB_CREDENTIALS= credentials('houssamtrizi-dockerhub')
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
            agent any
            steps{
                    sh 'docker build -t houssamtrizi/pythondocker_web:latest .'
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login - $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                    sh 'docker push houssamtrizi/pythondocker_web:latest'
            }
        }
    }
    post {
        always{
            cleanWs()
            node('builtin'){
                sh 'docker logout'

            }
        }
    }
}
