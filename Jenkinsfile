pipeline {
    agent any

    environment {
        // Set the full path to your Python executable
        PYTHON_EXE = 'C:\Users\Hp\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python\Python 3.14'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set Up Environment') {
            steps {
                bat '''
                    "%PYTHON_EXE%" -m venv venv
                    call venv\\Scripts\\activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
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