pipeline {
    agent any

    environment {
        VENV_DIR = "${WORKSPACE}/venv"
        PYTHONPATH = "${WORKSPACE}/src"
    }

    stages {
        stage('Setup') {
            steps {
                sh '''
                    python3 -m venv $VENV_DIR
                    . $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements-dev.txt
                    pip install pre-commit
                '''
            }
        }

        stage('Pre-commit Hooks') {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    git config --unset-all core.hooksPath || true
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
        always {
            echo '🧹 Finalizando build...'
        }

        success {
            echo '✅ Build finalizado com sucesso!'
        }

        failure {
            echo '❌ Build ou testes falharam!'
        }
    }
}
