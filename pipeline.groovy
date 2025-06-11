pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Compilando...'
      }
    }
  }

  post {
    success {
      echo 'Sucesso!'
    }
  }
}
