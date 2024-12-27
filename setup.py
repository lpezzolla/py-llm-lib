from setuptools import setup, find_packages

setup(
    name="py_llm_lib",
    version="0.2.0",
    description="A small a Python library designed to interact with Large Language Models",
    author="Luca Pezzolla",
    author_email="me@lucapezzolla.com",
    url="https://github.com/lpezzolla/py-llm-lib",
    packages=find_packages(where='src'),
    package_dir={'': 'src'}
)
