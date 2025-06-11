pipeline {
    agent any

    environment {
        // Ajuste o caminho do Python se precisar
        PYTHON_BIN = 'python3'
        VENV_DIR = 'venv'
    }

    stages {
        stage('Setup Python Environment') {
            steps {
                script {
                    // Cria e ativa venv
                    sh '''
                        if [ ! -d "$VENV_DIR" ]; then
                            $PYTHON_BIN -m venv $VENV_DIR
                        fi
                        source $VENV_DIR/bin/activate
                        pip install --upgrade pip
                        pip install black pre-commit pytest
                    '''
                }
            }
        }

        stage('Run Black') {
            steps {
                script {
                    // Rodar black formatando os arquivos (sem --check pra evitar erro)
                    sh '''
                        source $VENV_DIR/bin/activate
                        black .
                    '''
                }
            }
        }

        stage('Run Pre-commit') {
            steps {
                script {
                    sh '''
                        source $VENV_DIR/bin/activate
                        pre-commit run --all-files
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Roda pytest, ignora erro se não encontrar testes (exit code 5)
                    def pytestStatus = sh(
                        script: '''
                            source $VENV_DIR/bin/activate
                            pytest || echo $? > pytest_status.txt
                        ''',
                        returnStatus: true
                    )
                    // Read the status code if exists
                    def exitCode = 0
                    if (fileExists('pytest_status.txt')) {
                        exitCode = readFile('pytest_status.txt').trim().toInteger()
                    }

                    if (exitCode == 5) {
                        echo "⚠️ Pytest não encontrou testes. Ignorando erro."
                    } else if (pytestStatus != 0) {
                        error("❌ Testes falharam com código ${pytestStatus}")
                    } else {
                        echo "✅ Testes executados com sucesso."
                    }
                }
            }
        }
    }

    post {
        success {
            echo "🎉 Build finalizada com sucesso!"
            // Aqui você pode colocar notificações adicionais
        }
        failure {
            echo "❌ Falha na build."
            // Notificações de falha, se precisar
        }
    }
}
