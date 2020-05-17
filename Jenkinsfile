pipeline {
    agent any
    parameters {
        string(name: 'USER', defaultValue: 'VuK', description: 'Name of user')
        text(name: 'ADDRESS', defaultValue: '123 Easy St. Anaheim, CA', description: 'Enter some information about the person')
        booleanParam(name: 'TOGGLE', defaultValue: true, description: 'Toggle this value')
        choice(name: 'ENVIRONMENT', choices: ['DEV', 'STAGE', 'PROD'], description: 'stage environment')
        password(name: 'PASSWORD', defaultValue: 'SECRET', description: 'Enter a password')
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                echo "Hello ${params.USER}"
                echo "Your address: ${params.ADDRESS}"
                echo "Toggle: ${params.TOGGLE}"
                echo "Environment: ${params.ENVIRONMENT}"
                echo "Password: ${params.PASSWORD}"
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
    post {
      always {
        echo 'Initiating post processing steps'
      }
    }
}
