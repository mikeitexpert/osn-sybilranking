rm -rf build/*
rm -rf dist/*
python3 -m pip install  --upgrade setuptools wheel
python3 setup.py sdist bdist_wheel &&  pip uninstall SybilRanking-mikeitgeek -y && pip install --upgrade --force-reinstall dist/sybilranking_mikeitgeek-0.0.1-py3-none-any.whl
cp settings.json .pyenv/lib/python3.6/site-packages/SybilRanking/settings/settings.json
