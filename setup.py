# setup.py
from setuptools import setup, find_packages

setup(
    name="mobop2p",
    version="0.0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "mobop2p = main:main",
        ],
    },
)
