pipeline {
    agent any

    environment {
        VENV_DIR = "${env.WORKSPACE}/venv"
        PATH = "${env.WORKSPACE}/venv/bin:${env.PATH}"
    }

    stages {
        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv $VENV_DIR
                    . $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install black isort flake8 pytest pre-commit
                '''
            }
        }

        stage('Format Code') {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    black .
                    black --check .
                '''
            }
        }

        stage('Code Quality Checks') {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    isort --check-only .
                    flake8 .
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    pytest
                '''
            }
        }

        stage('Run Pre-commit Hooks') {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    pre-commit run --all-files
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Build and tests passed successfully!'
        }
        failure {
            echo '❌ Build or tests failed!'
            // Optionally notify GitHub or send alerts here
        }
    }
}
