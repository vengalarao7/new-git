pipeline {
    agent any
    stages {
        stage ("image build"){
            steps {
                sh "docker build -t flask-app ."
                sh "docker images |grep flask-app"
            }
        }
    }
}
