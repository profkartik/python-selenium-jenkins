pipeline {
    agent any

    environment {
        // Set the full path to your Python executable
        PYTHON_EXE = 'C:\Program Files\WindowsApps\PythonSoftwareFoundation.PythonManager_26.3.240.0_x64__3847v3x7pw1km'
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