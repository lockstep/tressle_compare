from setuptools import setup, find_packages

setup(
    name         = 'tressle_bot',
    version      = '1.0',
    packages     = find_packages(),
    entry_points = {'scrapy': ['settings = lib.settings']},
)
