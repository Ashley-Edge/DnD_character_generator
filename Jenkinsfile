pipeline {
    agent any
    environment {
            app_version = 'v1'
            rollback = 'false'
        } 
    stages{
        stage('AppTesting'){
            steps{
                sh './scripts/apptesting.sh'
            }
        }
        stage('Ansible'){
            steps{
                sh './scripts/ansible.sh'
            }
        }
        stage('Build-Images'){
            steps{
                sh 'docker login -u ashleyedge -p PeneloPig1989 dockerregistry.cloud.remote'
                sh './scripts/appbuild.sh'
            }
        }
        stage('Deploy-App'){
            steps{
                sh './scripts/appdeploy.sh'
            }
        }                   
        stage('NGINX'){
            steps{
                sh './scripts/nginx.sh'
            }
        }
    }
}