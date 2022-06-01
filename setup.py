from setuptools import setup, find_packages

setup(
    name='Pilar Flask API',
    version='1.0',
    long_description=__doc__,
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'Flask==2.1.2',
        'pytest==7.1.2'
    ]
)