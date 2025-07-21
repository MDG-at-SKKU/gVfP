from setuptools import setup, find_packages

setup(
    name="gVfP",
    version="0.0.2",
    python_requires='>=3.13',
    packages=find_packages(),
    install_requires=[
        "numpy",
        "ase"
    ],
    entry_points={
        "console_scripts": [
            "gvfp=genVESTAfromPOSCAR.main:main",
        ],
    },
)