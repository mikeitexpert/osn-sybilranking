python3 -m pip install  --upgrade setuptools wheel
python3 setup.py sdist bdist_wheel
pip install --upgrade --force-reinstall dist/sybilranking_mikeitgeek-0.0.1-py3-none-any.whl
