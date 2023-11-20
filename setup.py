import setuptools
import okx


setuptools.setup(
    name="okx",
    version=okx.__version__,
    author="Han Sanyue",
    author_email="hansanyue@hotmail.com",
    description="Python SDK for OKX",
    long_description_content_type="text/markdown",
    url="https://okx.com/docs-v5/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "importlib-metadata",
        "httpx[http2]",
        "keyring",
        "requests",
        "Twisted",
        "pyOpenSSL"
    ]
)