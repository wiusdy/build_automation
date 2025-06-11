pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        PYTHONPATH = 'src'
    }

    stages {
        stage('Setup Python') {
            steps {
                sh '''
                    python3 -m venv $VENV_DIR
                    . $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements-dev.txt
                    pip install pre-commit mypy black isort flake8 pytest
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

        stage('Run mypy') {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    export PYTHONPATH=$PYTHONPATH
                    mypy src --config-file mypy.ini
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
            echo '✅ Build and tests passed!'
        }
        failure {
            echo '❌ Build or tests failed!'
        }
    }
}
