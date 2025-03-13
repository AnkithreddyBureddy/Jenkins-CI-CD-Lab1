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
                sh 'python -m venv venv && source venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'source venv/bin/activate && python -m unittest test_todo.py'
            }
        }
        stage('Notify') {
            steps {
                mail to: 'your-email@example.com',
                     subject: 'Jenkins Build Notification',
                     body: 'Build completed successfully.'
            }
        }
    }
}
