# Automation API testing using Pyhton based on [restful-booker](https://restful-booker.herokuapp.com/)

This is a project for testing API using Python requests library.

### Prerequisites
In order to run these tests **Python 3** are needed

### Run project
Get clone from this repo.
Open cmd.
Run commands:
```
cd "the_repo_folder_path"
pip install pip
pip install -r requirements.txt
cd "tests"
```

Run tests:
* Just for run all of the tests put:
```
pytest
```
* For run tests with the report:
```
pytest --html=report.html
```
* For run pretests:
```
pytest -k ping
```
* For run rest of tests:
```
pytest -k "not ping"
```