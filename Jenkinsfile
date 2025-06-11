pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Setup Python Env') {
            steps {
                sh '''
                    python3 -m venv $VENV_DIR
                    . $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install black isort flake8 pre-commit pytest
                '''
            }
        }

        stage('Code Format Check') {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    black --check .
                    isort --check-only .
                    flake8 .
                '''
            }
        }

        stage('Pre-commit Hooks') {
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
            echo "✅ Build e testes finalizados com sucesso!"
        }
        failure {
            echo "❌ Falha na build ou testes!"
        }
    }
}
