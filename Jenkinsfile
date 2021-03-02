pipeline {
    agent any 
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
                sh './scripts/appbuild.sh' echo $?
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