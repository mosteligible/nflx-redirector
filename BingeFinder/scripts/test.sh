# /bin/bash

source venv-test/bin/activate

python -m unittest discover ./tests/
python tests/cleanup.py
