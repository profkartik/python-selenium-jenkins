pipeline {
    agent any

    environment {
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
                    echo [1/3] Creating virtual environment...
                    if exist venv rmdir /s /q venv
                    "%PYTHON_PATH%" -m venv venv

                    echo [2/3] Upgrading pip...
                    venv\\Scripts\\python.exe -m pip install --upgrade pip

                    echo [3/3] Installing pytest, selenium, and webdriver-manager...
                    venv\\Scripts\\python.exe -m pip install pytest selenium webdriver-manager
                    
                    echo Verifying pytest installation...
                    venv\\Scripts\\python.exe -m pytest --version
                '''
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat '''
                    @echo off
                    if not exist reports mkdir reports
                    
                    echo Running pytest test suite...
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