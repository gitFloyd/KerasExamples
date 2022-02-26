Welcome to SimpleServer Framework

The purpose of this project is to make it easy to run test code and display HTML formatted results in a browser.

To start the server, do the following on the command line:
python simpleServer.py

To access the home webpage, navigate to http://localhost:8082

To add python scripts as pages to the website, do the following:
In the same folder as simpleServer.py, add your python script. It must be named according to the convention that the name starts with "page_". Therfore, if I want to add a script "Test1", I would name the file "page_Test1.py". For each "page_<name>.py" script, the home page will display a link to that page.


simpleUtility is intended to provide simple utilities to help with testing. Currently, there is one function which can be imported to your testing scripts.

dump(var)
Input: one of the following -- str, int, list, tuple, set, or dict
Return: none
This function takes a list (or tuple, set, ...) and pretty prints it.