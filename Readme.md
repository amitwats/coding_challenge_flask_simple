# Coding Challenge


## Problem Statement
Develop a REST/JSON web API in Python or Java that accepts an array of numeric inputs and performs the following:

Finds the highest 3 numbers
Computes the square root of the sum of squares of the 3 highest numeric inputs. The following is an example input:
 
 ```sh
{
    “data”: [5,4,6,1]
}
```
 

The output expected would be:
```sh
{
    “output”: 8.77
}
```
 

Please use Maven to manage any dependencies if using Java. The code must make use of Python Lambda functions (https://book.pythontips.com/en/latest/map_filter.html) or Java Streams to compute the result. We encourage you to use the Spring framework if using Java, particularly to accelerate the development time for the web api. Please include unit tests

## Python Solution
This repository shows the solution in Python.

The following are the steps to execute the application in a windows based machine. You need to run all commands in a **PowerShell** window.


## Intial Setup
For initial setup, do the following
  * Run all commands from the application base folder
  * Create the virtual environment by running the command
    ```sh
    python -m venv venv
    ```
  * activate the virtual environment 

    ```sh
    venv\Scripts\activate
    ```
* Install all requirements

    ```sh
    py -m pip install -r requirements.txt
    ```

## Running the application

To start the flask server(local development only)
In Power shell, run the following commands from the base folder

```sh
$env:FLASK_APP="src/app.py"
flask run
```

To run the tests, from the base folder just run
```sh
pytest
```




