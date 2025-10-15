pipeline {
    agent { label 'slave1' }

    stages {
        stage('Setup') {
            steps {
                sh '''
                    
                    pwd
                    
                    ls
                    
                    # Create virtual environment
                    python3 -m venv venv

                    # Activate it
                    . venv/bin/activate

                    # Upgrade pip
                    pip install --upgrade pip

                    # Install dependencies
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest -v test_app.py
                '''
            }
        }

        stage('Integration Test') {
            steps {
                sh '''
                    . venv/bin/activate
                    pkill -f "python3 app.py" || true
                    pytest -v test_integration.py
                '''
            }
        }
    }
}
