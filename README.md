# Python-Skeleton-Projects
Project skeleton for python

Install the following Python packages: 
1. pip from http://pypi.python.org/pypi/pip 
2. distribute from http://pypi.python.org/pypi/distribute 
3. nose from http://pypi.python.org/pypi/nose 
4. virtualenv from http://pypi.python.org/pypi/virtualenv 

To use this skeleton project, rename directory "NAME" to your "PROJECT_NAME".

people commonly go into the tests/ directory to try to run fi les there, which won’t work. To run
your application’s tests, you would need to be above tests/ and this location I have above. Say
you try this:

$ cd tests/
$ nosetests
# WRONG! WRONG! WRONG!
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Ran 0 tests in 0.000s
OK

The correct way to test your script is, go to your root directory and run nosetests like this command :

$ cd .. # get out of tests/
$ ls # CORRECT! you are now in the right spot
NAME
bin
docs
setup.py
tests
$ nosetests
.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Ran 1 test in 0.004s
OK


