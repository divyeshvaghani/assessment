from setuptools import setup, find_packages

setup(
    name='DevOpsEngineerAssignment',
    version='0.1',
    packages=find_packages(where='src'),
    install_requires=[
        'boto3',
    ],
    entry_points={
        'console_scripts': [
            'DevOpsEngineerAssignment=src.main:main',
        ],
    },
)
