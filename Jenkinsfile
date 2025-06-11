pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
    }

    stages {
        stage('Setup Python') {
            steps {
                script {
                    // Criar e ativar venv
                    sh '''
                        python3 -m venv $VENV_DIR
                        . $VENV_DIR/bin/activate
                        pip install --upgrade pip
                        pip install black isort flake8 pytest pre-commit
                    '''
                }
            }
        }

        stage('Run Black') {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    black --check .
                '''
            }
        }

        stage('Run isort') {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    isort --check-only --skip $VENV_DIR .
                '''
            }
        }

        stage('Run Flake8') {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    flake8 --exclude=$VENV_DIR .
                '''
            }
        }

        stage('Run pre-commit hooks') {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    pre-commit run --all-files
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
    }

    post {
        success {
            echo '✅ Build and tests succeeded!'
        }
        failure {
            echo '❌ Build or tests failed!'
        }
    }
}
