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

        stage('Set Up Virtual Environment & Dependencies') {
            steps {
                bat '''
                    @echo off
                    echo Verifying Python executable...
                    "%PYTHON_PATH%" --version

                    if exist venv rmdir /s /q venv
                    "%PYTHON_PATH%" -m venv venv
                    call venv\\Scripts\\activate.bat
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat '''
                    @echo off
                    call venv\\Scripts\\activate.bat
                    if not exist reports mkdir reports
                    pytest tests/ --junitxml=reports/junit-report.xml
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