pipeline {
  agent any

  stages {
    stage('Instala dependências') {
      steps {
        sh 'python3 -m venv venv'
        sh '. venv/bin/activate && pip install -r requirements-dev.txt'
        sh '. venv/bin/activate && pip install black pre-commit pytest'
      }
    }

    stage('Executa build.sh') {
      steps {
        sh 'chmod +x build.sh'
        sh '. venv/bin/activate && ./build.sh'
      }
    }

    stage('PR Check') {
      when {
        expression {
          return env.CHANGE_ID != null
        }
      }
      steps {
        echo "✅ Essa build é de um Pull Request: ${env.CHANGE_ID}"
      }
    }
  }

  post {
    success {
      echo '✅ Build finalizado com sucesso!'
    }
    failure {
      echo '❌ Falha na build.'
    }
  }
}
