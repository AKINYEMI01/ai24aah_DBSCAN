from setuptools import setup, find_packages

setup(
    name="DBSCAN",  # Replace with your project name
    version="0.1.0",  # Version of your package
    author="Ilepe Akinyemi",
    author_email="ilepeakinyemi@gmail.com",
    description="A short description of your project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_project",  # GitHub repo URL
    packages=find_packages(),  # Automatically discover all packages in the directory
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "scikit-learn",
        "faker",
    ],  # List dependencies
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # Minimum Python version required
)

