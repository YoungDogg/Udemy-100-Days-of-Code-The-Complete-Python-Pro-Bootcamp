# Udemy 100 Days of Code: The Complete Python Pro Bootcamp

This repository contains the code and exercises from the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp".

## Table of Contents

- [Introduction](#introduction)
- [Cloning the Repository](#cloning-the-repository)
- [Setting Up the Virtual Environment](#setting-up-the-virtual-environment)
- [Installing Dependencies](#installing-dependencies)
- [Running the Project](#running-the-project)
- [Automated Dependency Installation](#automated-dependency-installation)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project contains various Python scripts and projects developed as part of the "100 Days of Code" challenge. Each day focuses on different aspects of Python programming, from basics to advanced topics.

## Cloning the Repository

To get started, clone the repository to your local machine using the following command:

```bash
git clone https://github.com/YoungDogg/Udemy-100-Days-of-Code-The-Complete-Python-Pro-Bootcamp.git
cd Udemy-100-Days-of-Code-The-Complete-Python-Pro-Bootcamp
```

## Setting Up the Virtual Environment
It's recommended to use a virtual environment to manage dependencies. Follow these steps to create and activate a virtual environment:

### Windows
```bash
python -m venv myenv
myenv\Scripts\activate
```
### macOS/Linux
```bash
python3 -m venv myenv
source myenv/bin/activate
```
## Installing Dependencies
Once the virtual environment is activated, install the required dependencies using the requirements.txt file:
```bash
pip install -r requirements.txt
```

## Running the Project
With the environment set up and dependencies installed, you can run any of the scripts or projects included in the repository. Navigate to the appropriate directory and execute the desired Python script:
```bash
python script_name.py
```
## Automated Dependency Installation
The project includes a Git hook to automate the installation of dependencies after pulling updates from the repository

### Windows
A post-merge Git hook script is included to automatically install dependencies:
- The `install_dependencies.bat` script is located at the project root and will be executed by the `post-merge` hook located in `.git/hooks`.
### How to Use
1. After pulling updates from Git, the hook will automatically run the `install_dependencies.bat` script to install/update dependencies.
2. Ensure the `install_dependencies.bat` script is executable.
### Content of install_dependencies.bat
```batch
@echo off
REM Activate the virtual environment
call myenv\Scripts\activate

REM Install/update dependencies
pip install -r requirements.txt

echo Dependencies installed/updated successfully.
```
### Content of .git/hooks/post-merge
```batch
@echo off
REM Run the dependency installation script
call install_dependencies.bat
```

## License
This project is licensed under the MIT License.
