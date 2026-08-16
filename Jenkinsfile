pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set Up Environment & Install') {
            steps {
                bat '''
                    python -m venv venv
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