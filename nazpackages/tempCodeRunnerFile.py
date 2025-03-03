# Import required functions
from setuptools import setup, find_packages

# Call setup function
setup(
    author="Nasrul Khair",
    description="A bundles of packages I'm saving to ease my daily tasks",
    name="nazpackages",
    version="0.1.0",
    packages=find_packages(include=["nazpackages", "nazpackages.*"])
)