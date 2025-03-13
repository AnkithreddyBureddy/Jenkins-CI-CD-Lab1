pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: 'github-pat', url: 'https://github.com/AnkithreddyBureddy/Jenkins-CI-CD-Lab1.git'
            }
        }
        stage('Setup') {
            steps {
                bat '''
                    python -m venv venv
                    venv\\Scripts\\activate
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                bat '''
                    venv\\Scripts\\activate
                    python -m unittest test_todo.py
                '''
            }
        }
        stage('Notify') {
            steps {
                mail to: 'Abureddy1900@conestogac.on.ca',
                     subject: 'Jenkins Build Notification',
                     body: 'Build completed successfully.'
            }
        }
    }
}
