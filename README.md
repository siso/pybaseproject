# Python Base Project

This can be used as a base for Python projects.

## Quickstart

Download sources:

```
git clone https://github.com/siso/pybaseproject
```

Amend changes to suit your needs:

- rename *pybaseproject* to your *PROJECT_NAME*
- rename *bin/pybaseproject* to *bin/YOUR_MAIN_SCRIPT_NAME*

Edit:

- bin/YOUR_MAIN_SCRIPT_NAME
- setup.py

Admittedly, the most interesting part is coding under *PROJECT_NAME* directory!

When you are done just run:

```
make all
```

to check and test sources, create pip and Debian packages.


## Makefile

*pybaseproject* comes with a basic *Makefile* which might comes in handy to speed up getting hands dirty.

Just run:

- ```make check```: check source codes
- ```make test```: run tests
- ```make source```: create a pip package (```python setup.py sdist```)
- ```make deb```: create Debian package
- ```make all```: run the above commands in one go


## Test with virtualenv

Create Python *virtual-environment* and install *pybaseproject*:

```
mkvirtualenv pybaseproject
cp /PATH/TO/pybaseproject/dist/pybaseproject-0.1.tar.gz .
tar xvfz pybaseproject-0.1.tar.gz
cd pybaseproject-0.1/
python setup.py install
```

execute it:

```
(pybaseproject)simone@nls206:~/tmp/20131103-115131/pybaseproject-0.1$ pybaseproject
pybaseproject.foo
Hola!
```

## Logging

Logging can be configured with 'logging.conf' (see **pybaseproject.foo**), or hardcoding settings directly in source code (easier to set up but harder to maintain).

### Coloured or non-coloured stdout

Logging to stdout supports ANSI-coloured output. To activate it **logging.conf** should look like:

```
[logger_root]
...
handlers=fileHandler,colouredConsoleHandler
```

If default black-and-white output is OK:

```
[logger_root]
...
handlers=fileHandler,consoleHandler
```

## Author

Simone Soldateschi - simone.soldateschi@gmail.com

## Links
- [Open Sourcing a Python Project the Right Way](http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/)
- [Structuring Your Project](http://docs.python-guide.org/en/latest/writing/structure/)
- [Learn Python The Hard Way - Exercise 46: A Project Skeleton](http://learnpythonthehardway.org/book/ex46.html)
- [Getting Started With setuptools and setup.py](http://pythonhosted.org/an_example_pypi_project/setuptools.html)
- [Installing python scripts](http://matthew-brett.github.io/pydagogue/installing_scripts.html)
- [What is the best project structure for a Python application?](http://stackoverflow.com/questions/193161/what-is-the-best-project-structure-for-a-python-application)
- [Good logging practice in Python](http://victorlin.me/posts/2012/08/26/good-logging-practice-in-python)
