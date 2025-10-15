pipeline {
    agent { label 'slave1' }

    stages {
        stage('Setup') {
            steps {
                sh '''
                    echo "--- Current Directory ---"
                    pwd
                    echo "--- List Files ---"
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
                    echo "--- Running Integration Test ---"
                    pkill -f "python3 app.py" || true
                    pytest -v test_integration.py
                '''
            }
        }
    }
}
