pipeline {
  agent { label 'build_automation_node' }

  stages {
    stage('Build') {
      steps {
        echo 'Building on agent...'
      }
    }

    stage('Test') {
      steps {
        echo 'Running tests...'
      }
    }
  }
}
