pipeline {
    agent any
    stages {
        stage {
            sh "docker build -t flask-app ."
            sh "docker images |grep flask-app"
        }
    }
}