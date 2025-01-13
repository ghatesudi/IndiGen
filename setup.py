from setuptools import setup, find_packages

setup(
    name='indigen',
    version='0.1',
    packages=find_packages(include=["indigen", "indigen.*"]),  # Automatically find submodules
    include_package_data=True,
    author="Sudeep Ghate",
    author_email="sudeep1129@gmail.com",  # Add a valid email
    description="A package for generating synthetic names based on Indian states.",
    url="https://github.com/ghatesudi/indigen",  # Add a valid project URL
    entry_points={
        "console_scripts": [
            "indigen=indigen.scripts.indigen:main",  # Reference your script's main function
        ],
    },
)
