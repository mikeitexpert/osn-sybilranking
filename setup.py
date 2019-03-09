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
    url="https://github.com/mikeitexpert/osn-sybilranking",
    packages=setuptools.find_packages(),
    # packages=['SybilRanking'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data = True,
    # package_data={
    #     'SybilRanking': ['*.csv'],
    # },
    # data_files=\
    #     [
    #         ('modelfiles', ['SybilRanking/model/modelfiles/TwitterNaiveBayesSybilRanker.joblib',
    #                         'SybilRanking/model/modelfiles/InstaNaiveBayesSybilRanker.joblib']),
    #         ('traindata', ['SybilRanking/model/traindata/insta_train_data.csv',
    #                        'SybilRanking/model/traindata/twitter_train_data.csv']),
    #         ('settings', ['SybilRanking/settings/settings.json']),
    #         ('scraper', ['SybilRanking/scraper/InstagramScraper.py']),
    #         ('test', ['SybilRanking/test/test_twitter_naivebayes_ranker.py',
    #                     'SybilRanking/test/test_twitter_naivebayes_ranker_factory.py',
    #                     'SybilRanking/test/test_insta_naivebayes_ranker_factory.py',
    #                     'SybilRanking/test/scraper/test_insta_scraper.py',
    #                     'SybilRanking/test/test_insta_naivebayes_ranker.py'
    #         ])
    #     ],
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
        'tqdm',
    ],
)
