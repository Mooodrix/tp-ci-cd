pipeline {
    agent any

    stages {
        stage('Installation Python') {
            steps {
                // On installe Python à la volée dans notre serveur Jenkins
                sh '''
                apt-get update
                apt-get install -y python3 python3-pip python3-venv
                python3 -m venv venv
                '''
            }
        }

        stage('Build & Tests') {
            steps {
                // On lance les tests et on génère le rapport "coverage.xml" pour SonarQube
                sh '''
                . venv/bin/activate
                pip install -r requirements.txt
                coverage run -m pytest test_product_manager.py
                coverage xml
                radon cc product_manager.py -a
                '''
            }
        }

        stage('Analyse SonarQube') {
            environment {
                // On appelle l'outil qu'on vient juste d'ajouter à l'étape 1
                SCANNER_HOME = tool 'sonar-scanner'
            }
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh "${SCANNER_HOME}/bin/sonar-scanner -Dsonar.projectKey=tp-ci-cd -Dsonar.sources=. -Dsonar.python.coverage.reportPaths=coverage.xml"
                }
            }
        }
    }
}