## Packages

* python (v2.7.x or any compatible implementation, i.e. pypy)
* python-virtualenv
* python-pip

## Clone the git repository

`git clone git@github.com:folz/HackU11.git HackU11 && cd HackU11`

## Set up Virtualenv

Create a [pip](http://pypi.python.org/pypi/pip) requirements file that declares our use of Django:

**requirements.txt**

> Django==1.3
> 
> psycopg2==2.4.2


Create a [Virtualenv](http://pypi.python.org/pypi/virtualenv):

`$ virtualenv --no-site-packages .`

> New python executable in ./bin/python
> 
> Installing setuptools............done.


Before running pip (or the application), you’ll need to source the Virtualenv environment:

`$ source bin/activate`

This will change your prompt to include the project name. (You must source the virtualenv environment for each terminal session where you wish to run your app.)

Install dependencies with pip:

`$ pip install -r requirements.txt`

> Downloading/unpacking psycopg2==2.4.2 (from -r requirements.txt (line 2))
> 
> Downloading psycopg2-2.4.2.tar.gz (667Kb): 667Kb downloaded
> 
> Running setup.py egg_info for package psycopg2
> 
>   no previously-included directories found matching 'doc/src/_build'
> 
> Downloading/unpacking Django==1.3 (from -r requirements.txt (line 1))
> 
> Downloading Django-1.3.tar.gz (6.5Mb): 6.5Mb downloaded
> 
> Running setup.py egg_info for package Django
> 
> Installing collected packages: Django, psycopg2
> 
> ...
> 
> Successfully installed Django psycopg2
> 
> Cleaning up...

Now the Django app should be runnable. Test to make sure the application runs:

`$ python HackU11/manage.py runserver`

> Validating models...
> 
> 
> 
> 0 errors found
> 
> Django version 1.3, using settings 'HackU11.settings'
> 
> Development server is running at http://127.0.0.1:8000/
> 
> Quit the server with CONTROL-C.

Ctrl-C to exit the server.