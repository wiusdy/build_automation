pipeline {
  agent { label 'build_automation_node' }

  stages {
    stage('Build') {
      steps {
        echo "Build for PR branch: ${env.BRANCH_NAME}"
      }
    }
    stage('Test') {
      steps {
        echo "Running tests..."
      }
    }
  }
}
