pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: 'github-pat', url: 'https://github.com/AnkithreddyBureddy/Todo-List.git'
            }
        }

        stage('List Files') {
            steps {
                bat 'dir'  // List files in the current workspace for debugging
            }
        }

        stage('Setup') {
            steps {
                script {
                    // Set up a virtual environment
                    bat 'C:\\Users\\dell\\AppData\\Local\\Programs\\Python\\Python36-32\\python -m venv venv'
                    bat 'venv\\Scripts\\pip install -r requirements.txt'  // Install dependencies
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    echo "Building the application..."
                    bat 'venv\\Scripts\\python --version'  // Verify Python version
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo "Running tests..."
                    bat 'venv\\Scripts\\python -m unittest test_todo.py'  // Run unit tests for To-Do app
                }
            }
        }

        stage('Notify') {
            steps {
                script {
                    echo "Sending email notification..."
                    mail to: 'Abureddy1900@conestogac.on.ca',
                         subject: "Jenkins Build Notification",
                         body: "The Jenkins build has completed. Check Jenkins for details."
                }
            }
        }
    }

    post {
        success {
            echo "Build was successful!"
        }
        failure {
            echo "Build failed!"
        }
    }
}
