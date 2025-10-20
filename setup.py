# setup.py
from setuptools import setup, find_packages

setup(
    name="MoboP2P",
    version="0.0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "textual"
    ],
    entry_points={
        "console_scripts": [
            "mobop2p = main:main",
        ],
    },
)
