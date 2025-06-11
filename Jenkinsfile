pipeline {
  agent any

  environment {
    BUILD_TYPE = "PR"
  }

  stages {
    stage('PR Check') {
      when {
        expression {
          // Só executa se a build estiver associada a um Pull Request
          return env.CHANGE_ID != null
        }
      }
      steps {
        echo "✅ Essa build é de um Pull Request: ${env.CHANGE_ID}"
      }
    }

    stage('Build') {
      steps {
        echo "🚧 Etapa de build em execução..."
        // sh './build.sh' (exemplo)
      }
    }

    stage('Test') {
      steps {
        echo "🧪 Executando testes..."
        // sh './run-tests.sh'
      }
    }
  }

  post {
    success {
      echo '✅ Build finalizado com sucesso!'
    }
    failure {
      echo '❌ O build falhou.'
    }
  }
}
