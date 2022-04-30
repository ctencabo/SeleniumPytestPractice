# SeleniumPytestPractice
Selenium Pytest Practice

### Installation

**Pre-requisite**

- Python (3.7 and above are recommended)
- Install Pip after installing Python

**Setting-up**

- Clone this repository
- Create a virtualenv by running `python -m venv [name_of_virtual_env]`
- Activate the virtualenv by running:
   - `[name_of_virtual_env]\Scripts\activate.bat` for Windows
   - `source [name_of_virtual_env]\activate` for Linux
- Install needed requirements by running `pip install -r requirements.txt`

**Running Tests**

- Tests are run using pytest
  - Use the command `pytest -v -s` to run all test cases under the repository
  - To run specific tests, you can include the path of the file like this: `pytest -v -s [path_of_test.py]` 
