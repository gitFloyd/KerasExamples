# Welcome to SimpleServer Framework

## Purpose
The purpose of this project is to make it easy to run test code and display HTML formatted results in a browser.

## Get Started
#### Starting the server
To start the server, do the following on the command line:
python simpleServer.py

#### Accessing the server
To access the home webpage, navigate to http://localhost:8082

#### Adding scripts
To add python scripts as pages to the website, do the following:
In the same folder as simpleServer.py, add your python script. It must be named according to the convention that the name starts with "page_". Therfore, if I want to add a script "Test1", I would name the file "page_Test1.py". For each "page_<name>.py" script, the home page will display a link to that page.

## Additional utilities
#### About simpleUtility
simpleUtility is intended to provide simple utilities to help with testing. Currently, there is one function which can be imported to your testing scripts.

### Functions:

#### dump(var)
Input: one of the following -- str, int, list, tuple, set, dict, Numpy Array
Return: none
This function takes a list (or tuple, set, ...) and pretty prints it.

#### printbr(str)
Input: a string to convert \n or \r\n to <br>
Return: none
This function converts newline characters to <br>
and then invokes print(str_with_br)

#### has_tf_and_gpu()
Return: bool
Is tensorflow available and does it
have access to the gpu?

## Updates
### 2022-02-27
- Added documentation of simpleUtility to this README.
- Added server.bat for folks on Windows to easily start up the server by executing server.bat
- Updated styles for links in test.css
- Changed the way links to pages are displayed by removing the ".py". Therefore, pages can be named something like: page_My Fancy Page Title.py and the link will look like: My Fancy Page Title

