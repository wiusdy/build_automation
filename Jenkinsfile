pipeline {
  agent { label 'build_automation_node' }

  environment {
    // Pode adicionar variáveis de ambiente aqui, se necessário
    APP_ENV = 'development'
  }

  options {
    // Mantém os últimos 5 builds apenas
    buildDiscarder(logRotator(numToKeepStr: '5'))
    // Exibe timestamps no log
    timestamps()
  }

  triggers {
    // Usado apenas para debugging (scan periódico), mas GitHub Webhook é preferível
    pollSCM('* * * * *') // Opcional: verifica por mudanças a cada minuto
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
        echo "Branch atual: ${env.BRANCH_NAME}"
      }
    }

    stage('Build') {
      steps {
        echo '🛠️ Rodando processo de build...'
        // Exemplo: build Node, Java, Docker etc.
        sh 'echo "Simulando build..."'
      }
    }

    stage('Test') {
      steps {
        echo '🧪 Executando testes...'
        sh 'echo "Rodando testes fictícios"'
      }
    }

    stage('PR Check') {
      when {
        expression {
          // Só executa se a branch tiver um PR associado (GitHub multibranch trata isso)
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
