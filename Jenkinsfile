pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Set Up Environment') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            python3 -m venv venv
                            . venv/bin/activate
                            pip install --upgrade pip
                            pip install -r requirements.txt
                        '''
                    } else {
                        bat '''
                            python -m venv venv
                            call venv\\Scripts\\activate
                            python -m pip install --upgrade pip
                            pip install -r requirements.txt
                        '''
                    }
                }
            }
        }

        stage('Run Selenium Tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            . venv/bin/activate
                            mkdir -p reports
                            pytest tests/ --junitxml=reports/junit-report.xml || true
                        '''
                    } else {
                        bat '''
                            call venv\\Scripts\\activate
                            if not exist reports mkdir reports
                            pytest tests/ --junitxml=reports/junit-report.xml
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            // Parses test reports and creates trend graphs in Jenkins
            junit testResults: 'reports/junit-report.xml', allowEmptyResults: true
        }
    }
}
