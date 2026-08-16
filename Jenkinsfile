pipeline {
    agent any

    environment {
        // Point to your exact Python binary path
        PYTHON_PATH = 'C:\\Users\\Hp\\AppData\\Local\\Python\\bin\\python.exe'
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Set Up Environment & Dependencies') {
            steps {
                bat '''
                    @echo off
                    echo Setting up virtual environment...
                    if exist venv rmdir /s /q venv
                    "%PYTHON_PATH%" -m venv venv
                    
                    echo Installing required packages...
                    venv\\Scripts\\python.exe -m pip install --upgrade pip
                    venv\\Scripts\\python.exe -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat '''
                    @echo off
                    if not exist reports mkdir reports
                    
                    echo Running pytest...
                    venv\\Scripts\\python.exe -m pytest tests/ --junitxml=reports/junit-report.xml
                '''
            }
        }
    }

    post {
        always {
            junit testResults: 'reports/junit-report.xml', allowEmptyResults: true
        }
    }
}