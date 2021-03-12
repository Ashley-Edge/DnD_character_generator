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
                docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials'){
                    sh './scripts/appbuild.sh'
                }
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