# Import required functions
from setuptools import setup, find_packages  # Make sure find_packages is imported

# Call setup function
setup(
    author="Nasrul Khair",
    description="A bundle of packages I'm saving to ease my daily tasks",
    name="nazpackages",
    version="0.1.0",
    packages=find_packages(include=["nazpackages", "nazpackages.*"])  # Corrected find_packages
)
