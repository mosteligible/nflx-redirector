# /bin/bash

python3 -m venv venv-test
source venv-test/bin/activate

pip install --upgrade pip --no-cache-dir
pip install -r requirements.txt --no-cache-dir
