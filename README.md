# Introduction
SybilRanking is a python package to both identify and rank Sybil nodes in a social network using public social medial (eg. Twitter, Instagram, etc) or any other method.

To be more specific, we aim at investigating / prototyping techniques and algorithms to measure authenticity of users (representing a human) as defined by [BrightID](https://www.brightid.org/). In short according the [BrightID Whitepaper](https://docs.google.com/document/d/1dlQDz8SyOcXtR8azNVDBA3MiElNuTneuU5Uu5RQG55s/edit): "BrightID seeks to provide everyone with the benefits of being verified as a unique person--namely, greater access to money, honest information, and greater choice in government."



# How to install
The same way as a regular python package
```
python setup.py install
```
or
```
pip install --upgrade --force-reinstall dist/sybilranking_mikeitgeek-0.0.1-py3-none-any.whl
```

# How to configure
All settings are done using ```settings/settings.json``` file located in the package folder where installed.

```
{
	"proxies": {"http": "http://127.0.0.1:2080", "https": "https://127.0.0.1:2080"},
	"twitter_access_token": "blabal_twitter_access_token",
	"insta_username": "scraper_instagram_username",
	"insta_password": "scraper_instagram_username"
}
```
* proxies: proxies settings.
* twitter_access_token: twitter access token to connect twitter API to scrape the user details.
* insta_username: the instagram username to scrape the user details (the target user needs to in the `following` list of insta_username).
* insta_password: the password for insta_username.


# How to run and test
There is test sub-package you could use to test different methods as developed. To test all, do as follows:

```
python -c "import SybilRanking; SybilRanking.test.doAllTest()"
```


# What methods have been considered so far
* Bernoulli Naive Bayes
* Deep Neural Network (DNN) Estimators

New AI/ML methods are on the way.

# What social media have been considered so far
* Twitter
* Instagram

# How to build the package
You can use the below command to build the whl package or simply use build.sh to build the package.

```
python3 setup.py sdist bdist_wheel && pip install --upgrade --force-reinstall dist/sybilranking_mikeitgeek-0.0.1-py3-none-any.whl
```

# Example Package

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.
