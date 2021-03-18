from setuptools import setup

setup(
    name='PyUploadGram',
    version='1.0.0',
    project_urls={"Source": "https://github.com/scrubjay55/PyUploadGram.git"},
    url="https://github.com/scrubjay55/PyUploadGram.git",
    author='scrubjay55',
    license="APLv2",
    packages=['PyUploadGram'],
    description='An API wrapper for UploadGram',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        "requests",
    ],
)
