import setuptools
from glob import glob

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sybilranking-mikeitgeek",
    version="0.0.1",
    author="Mike IT Geek",
    author_email="mikeitgeek@gmail.com",
    description="Sybil ranking package to mitigate Sybil attacks and rank Sybil nodes in socail media networks using public socail media such as Twitter, Instagram.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    # packages=['SybilRanking'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data = True,
    package_data={
        'SybilRanking': ['*.csv'],        
    },
    data_files=\
        [
            ('modelfiles', ['SybilRanking/model/modelfiles/TwitterNaiveBayesSybilRanker.joblib']),
            ('settings', ['SybilRanking/settings/settings.json']),
        ],
    install_requires=[
        'certifi',
        'chardet',
        'idna',
        'joblib',
        'numpy',
        'pandas',
        'pip',
        'python-dateutil',
        'pytz',
        'requests',
        'scikit-learn',
        'scipy',
        'setuptools',
        'six',
        'sklearn',
        'sybilranking-mikeitgeek',
        'urllib3',
        'wheel',
    ],    
)
