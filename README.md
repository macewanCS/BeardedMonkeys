# README

- [Specs](https://github.com/macewanCS/BeardedMonkeys/blob/master/specs/specs.md)
- [Mock-ups](https://github.com/macewanCS/BeardedMonkeys/tree/master/specs/mockups)
- [User Stories](https://github.com/macewanCS/BeardedMonkeys/blob/master/specs/stories.md)
- [PowerPoint Slides](https://github.com/macewanCS/BeardedMonkeys/blob/master/specs/BeardedMonkeys-%20Presentation.pptx)

### Step by Step Build:
Please follow the following steps in order to get up and running with our web application,

- Download the source files from github by running `git clone https://github.com/macewanCS/BeardedMonkeys.git`

- Go to the folder you wish to have your virtual environment installed, and run `virtualenv -p /usr/bin/python3.4 virtual_environment_name`

- Activate the virtual environment by running `source virtual_environment_name/bin/activate`

- Once the virtual environment is activated, if it is the first time, you may need to install Django. You can do so by simply running `pip install Django`

- You may verify the installed version of python and Django. To find out python version run `python --version`. For Django run `python manage.py --version`. Python version should be `3.4` and Django `1.10` is preferred.

- After installing the Django in your virtual environment, run `python manage.py migrate` to build the app. Note: In few cases, you may have to run `python manage.py makemigrations` before doing this step. For more information, please refer to the [Django documentation](https://docs.djangoproject.com/en/1.10/topics/migrations/).

- To run the server the command is, `python manage.py runserver`

- You may now access the web application by going to the url [localhost:8000](localhost:8000)

- To create a new user, run `python manage.py createsuperuser`

- Admin Access will be available at [localhost:8000/admin](localhost:8000/admin). You could add user, assign status and branch for each user in the admin pane

- Note: We have made the branches dynamic. What it means is that whenever we assign a user to a branch, it will automatically adds that branch for "tickets filtration". No hard coding of branches required in order to make them appear in filtration options.

**Important Note:** Please be sure to setup the branch for each user you create from the admin panel. Otherwise it will give you 404 Does not exist error for the user. For more information on that error, please watch the video tutorial on Localhost Setup, starting at 7m10s.

### Localhost Setup:

https://www.youtube.com/watch?v=q03YCMWPIhg

### Few Useful Git Commands:
- When pushing your files, make sure you are in your own forked repository, not the group main repository. Run, `git remote show origin`
- Cache credential for an hour, `git config --global credential.helper 'cache --timeout=3600'`
- Add remote upstream, `git remote add upstream http://link-to-repo`
- check configured remote repository, `git remote -v`

# We are BeardedMonkeys

## Members
- [Hafiz Temuri](https://github.com/temurih)
- [Connor Dykstra](https://github.com/DykstraC7)
- [Mohammed Alhamood](https://github.com/alhamoodm)
- [Abdullah Alshakhs](https://github.com/abdullah1413)

### Hafiz Temuri
Hi, I am Hafiz Temuri and I am a computer science student. I used to be crazy passionate about ethical hacking since I was in high school, and that lead me computer science. Once I got into the field, I become more interested in web design and development.

I have been using core web languages such as HTML, CSS, JavaScript and jQuery for quite a few years. Also, I am a great supporter of WordPress, that means I like to design/develop it's templates and plugins. I am a huge fan of Adobe Creative Design, and I use Adobe Photoshop, Illustrator, After Effects, Premier Pro, InDesign depending on the project. My knowledge of programming language extend to Python, C language, Java, Ruby, VB.net PHP and SQL. I just like to taste everything.

You can checkout my current websites to know me better, [webpro.tech](http://www.webpro.tech/) and [Search Beast](https://www.searchbeast.ca/)

### Abdullah Alshakhs
I am Abdullah, and I am here to attend the CMPT395 lab and learn more about github and its feature. 

### Connor Dykstra
I am Connor Dykstra, and I'm not interested in saying anything interesting about myself.

### Mohammed Al Hamood
i am Mohammed , and i am here in thursday lab lering how to use github.and i like to cude using C#.
