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
            call "C:\\Users\\dell\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe" -m venv venv
            call venv\\Scripts\\activate.bat
            call "C:\\Users\\dell\\AppData\\Local\\Programs\\Python\\Python36-32\\Scripts\\pip.exe" install -r requirements.txt
        '''
    }
}

        stage('Test') {
            steps {
                bat '''
                    call venv\\Scripts\\activate.bat
                    "C:\\Users\\dell\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe" -m unittest test_todo.py
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
