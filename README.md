# Welcome to SimpleServer Framework

## Purpose
The purpose of this project is to make it easy to run test code and display HTML formatted results in a browser.

## Get Started
#### Starting the server
To start the server, do the following on the command line:<br>
python simpleServer.py

#### Accessing the server
To access the home webpage, navigate to http://localhost:8082

#### Adding scripts
To add python scripts as pages to the website, do the following:<br>
In the same folder as simpleServer.py, add your python script. It must be named according to the convention that the name starts with "page_". Therfore, if I want to add a script "Test1", I would name the file "page_Test1.py". For each "page_&lt;name&gt;.py" script, the home page will display a link to that page.

## Additional utilities
#### About simpleUtility
simpleUtility is intended to provide simple utilities to help with testing. Currently, there is one function which can be imported to your testing scripts.

### Functions:

#### dump(var, tab_size)
Input: one of the following -- str, int, list, tuple, set, dict, Numpy Array<br>
Return: none<br>
This function takes a list (or tuple, set, ...) and pretty prints it.

#### printbr(str)
Input: a string to convert \n or \r\n to &lt;br&gt;<br>
Return: none
This function converts newline characters to &lt;br&gt;<br>
and then invokes print(str_with_br)

#### has_tf_and_gpu()
Return: bool<br>
Is tensorflow available and does it have access to the gpu?

## Updates
### 2022-02-28
- test.css
	- Added some addition style rules to main element
- base.css
	- This is a new css file and is included in the header by default
	- It contains basic utility styles
	- Currently, it has .hidden
- simpleUtility
	- Add TextWrapper class. It facilitates wrapping outputted text in a specified HTML tag. It optionally takes an HTMLElement class attribute. If adding the classes foo and bar, simply pass in "foo bar".
	- Add Hide and Pre classes which inherit from TextWrapper. Hide puts outputted text in a hidden div, and Pre puts outtputted text inside of &lt;pre&gt; tags.
	- nl2br(text) function added. Previously, printbr() converted \n and \r\n to &lt;br&gt; and printed the results right away. Now, nl2br() handles the conversion. Then printbr() just does the printing. printbr() is still used as before. It is only the internal code that changed.
	- Code for a Keras tutorial was added.
		- Filename: page_First Keras Tutorial.py
		- Find the tutorial here: https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/
		- The code in this file is an implementation of that tutorial using simplerServer style.
### 2022-02-27
- Added documentation of simpleUtility to this README.
- Added server.bat for folks on Windows to easily start up the server by executing server.bat
- Updated styles for links in test.css
- Changed the way links to pages are displayed by removing the ".py". Therefore, pages can be named something like: page_My Fancy Page Title.py and the link will look like: My Fancy Page Title

