pipeline {
    agent any

    stages {
        stage('Run Python') {
            steps {
                bat 'python --version'
                bat 'python app.py'
            }
        }
    }
}