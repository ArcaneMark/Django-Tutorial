01 Install Python
02 Set up a database
03 Install Django #better install after you create a virtualenvironment

04 Verify Installation
  #type 'python' in the shell to check python version
  #type 'import django' in python environment
  #type 'print(django.get_version())'

"""
Below is the guide with Virtual Environment
"""
01. install first virtualenvironment wrapper
$pip install virtualenvwrapper-win

02. create a virtual virtualenvironment
$mkvirtualenv py2 #py2 is the virtual environment name
#$rmvirtualenv py2 if you want a virtual environment to be removed

03. work on your virtual environment
$workon py2 #py2 is the virtual environment name

04. install django
$pip install django

05. create a project
$django-admin startproject djangoproject #djangoproject is the project name

06. install mysqlclient
$pip install mysqlclient mysqlclient-1.3.13-cp37-cp37m-win32.whl

07. make sure you installed your mysql workbench

08. configure your django
