Note: Before you can run the django server, you should create your virtual environment folder (i.e. the "venv" folder) at the directory level of THIS readme file. Use this command (should do this only once):

virtualenv -p /usr/bin/python3.4 venv


If something goes wrong, make sure python 3.4 is installed, and that virtualenv is installed. Next, activate your virtual environment (named 'venv') BEFORE installing Django:

source venv/bin/activate

Using the virtual environment:
Now whenever you want to run or do anything with the Django server, you simply need to run:

source venv/bin/activate

at this directory level, and then the shell you're using will be able to issue all python commands correctly for Django until you close it.

Finally, you can install Django using this command (should only do once):

pip install Django

Then run,

python manage.py migrate
