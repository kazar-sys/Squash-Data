from setuptools import setup, find_packages

setup(
    name="squash_rank",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'pandas',
        'openpyxl',
        'scipy',
        'numpy',
        'plotly',
    ],
    entry_points={
        'console_scripts': [
            'generate-my-dashboard=src.main:run', 
        ],
    },
)