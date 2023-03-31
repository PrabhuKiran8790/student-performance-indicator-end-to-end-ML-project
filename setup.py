from setuptools import setup, find_packages


get_requirements = lambda file: [line.strip() for line in open(file).readlines()][:-1] # Ignore last line (-e .)


setup(
    name="Student Performance Indicator",
    version="0.1",
    author="Prabhu Kiran Konda",
    author_email="prabhukiran426@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
