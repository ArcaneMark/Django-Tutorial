01 Install Python
02 Create A Virtual Environment for a Project
03 ALWAYS WORKON THAT ENVIRONMENT
04 Install Django
05 Setup Your Database (create a new schema for the project)
06 Install Mysql Client (for MySQL)
07 Make sure that you are in the working environment (virtual env)
08 Create the project --> django-admin startproject mysite
09 Test the Django Webserver --> python manage.py runserver
10 Create your App --> python manage.py startapp polls

----------------------------------------------------------------------
11 Configure your App views.py

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
----------------------------------------------------------------------

----------------------------------------------------------------------
12 Create urls.py on your app directory and configure it
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
----------------------------------------------------------------------

----------------------------------------------------------------------
13 At your root URL (urls.py not under your app but under your root project folder), point it to your app url
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
----------------------------------------------------------------------

----------------------------------------------------------------------
14 Run the web server again --> python manage.py runserver and open your localhost web browser under your app folder eg. http://localhost:8000/polls/
you must get the define HttpResponse if configured successfully
----------------------------------------------------------------------

----------------------------------------------------------------------
15 Setup Your Database Configuration under your project settings.py. Below is an example configuration for MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DjangoTutorial', #make sure this Schema has been defined already in your mysql
        'USER': 'SuperMark',
        'PASSWORD': 'letmeenter@dear',
        'HOST': '35.240.201.48',
        'PORT': ''
    }
}
----------------------------------------------------------------------

----------------------------------------------------------------------
16 To add the tables needed for the default Django Installed APPS such as
django.contrib.admin – The admin site. You’ll use it shortly.
django.contrib.auth – An authentication system.
django.contrib.contenttypes – A framework for content types.
django.contrib.sessions – A session framework.
django.contrib.messages – A messaging framework.
django.contrib.staticfiles – A framework for managing static files.

run this migrate command --> python manage.py migrate
----------------------------------------------------------------------

----------------------------------------------------------------------
17 Define Your Models – essentially, your database layout, with additional metadata.
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
----------------------------------------------------------------------

----------------------------------------------------------------------
18 To activate your model make sure you add your app in INSTALLED_APPS in your site settings.py
with this you will let Django knows to include the polls app.

INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
----------------------------------------------------------------------

----------------------------------------------------------------------
19 run this --> python manage.py makemigrations polls
you will see like this. You can view as well your planed schema in polls/migrations/0001_initial.py
remember these are just plans and not yet committed in your database

Migrations for 'polls':
  polls/migrations/0001_initial.py:
    - Create model Choice
    - Create model Question
    - Add field question to choice
----------------------------------------------------------------------

20 run this --> python manage.py sqlmigrate polls 0001
this will let you see its equevalent mysql command or query
remember this is only showing you a mysql representation of your planned schema and it is not yet committed to your database

21 to make sure that everything is fine before touching or committing your planned changes to your database
run this first --> python manage.py check

22 run this --> python manage.py migrate
this wil now apply your models to your database

23 now you can play the Django API
please see below for more information and commands:
https://docs.djangoproject.com/en/2.1/ref/models/relations/
https://docs.djangoproject.com/en/2.1/topics/db/queries/#field-lookups-intro
https://docs.djangoproject.com/en/2.1/topics/db/queries/

24 now create a superuser for your Django Admin
run this --> python manage.py createsuperuser
enter the username, email, and password

25 run the webserver --> python.py manage.py runserver
go to /admin/ in your localhost in your browser and you can enter it with your superuser credentials

----------------------------------------------------------------------
26 you will noticed that the admin site will not show any of your apps objects
to make your objects appear, go to your app admin.py and edit it like below

from django.contrib import admin
from .models import Question
admin.site.register(Question)

now you will see in your admin the Question object and you can modify it by clicking its link
----------------------------------------------------------------------

27 add the html files that will render your views. make a practice of adding it to another folder after creating a template folder
like polls/templates/polls/index.html

----------------------------------------------------------------------
28 you can add or define views in your apps' views.py as many as you want such as
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.http import Http404

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request,'polls/index.html',context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'polls/detail.html',{'question':question})

    return render(request,'polls/detail.html',{'question': question})

def results(request, question_id):
    response = "You're looking at the result of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

----------------------------------------------------------------------

----------------------------------------------------------------------
29 whenever you define views, wire this to your app urls
from django.urls import path

from . import views

#lets specify the app name as your url names can be use for other apps.
#you should specify as well this app name on your url name tags in your template
app_name = 'polls'
urlpatterns = [
    #the name or 3rd parameter is very useful in your template file in using the {% url %} template tag
    path('', views.index, name='index'), #/polls/
    path('detail_specifics/<int:question_id>/', views.detail, name='detail'), #/polls/3
    path('<int:question_id>/results/', views.results, name='results'), #/polls/3/results/
    path('<int:question_id>/vote/', views.vote, name='vote'), #/polls/3/vote/

]
-------------------------------------------------------------------

-------------------------------------------------------------------
30 You can design your template with Jinja Codes such as what is in the detail.html

<h1>{{ question.question_text }}</h1>

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
{% for choice in question.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
{% endfor %}
<input type="submit" value="Vote">
</form>
-------------------------------------------------------------------

-------------------------------------------------------------------
31 Learn to simplify views by using Generic Views but first ammend the URL
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
-------------------------------------------------------------------

-------------------------------------------------------------------
32 Now let us ammend views (This will simplify your coding for views but remember to ammend first the URLs like in step #31)
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    ... # same as above, no changes needed.
-------------------------------------------------------------------

33 Make a testcase. You can create it under your apps folder with file-name tests.py

34 Create a static folder under your apps folder. from there you can put your css and images.

35 Customize the admin form by:
-reording the fields on the order of admin.site.register in app admin.py
-you can split the field into fieldsets
-you can add related objects as the django can automatically detect foreignkey which will be represented with a select box
-you can instruct django to include related object on a single page
-you can shoice the layout with fieldsets
-you can add other arbitrary field such as other functions in your objects that return values corresponding to an item
-you can add filter and specify field to filter
-you can add search box and specify field to search

-------------------------------------------------------------------
35 you can customize the admin base html
-add a templates directory with same level of your app manage.py or under your project directory
-on your project settings.py, supply path for your DIRS
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
-------------------------------------------------------------------

36 copy your django base_site.html from django templates default folder to the project created templates folder (folder same level with manage.py)
-to know the default folder you can type --> python -c "import django; print(django.__path__)"

37 you can the same approach to other default html file if you want to customize it

38 Package your file as reusable apps so it can be installed as libararies (***successfully done this with virtualenvironment)
-you can move your apps directory outside of your project
-create a folder corresponding a name of your app
-make sure the name of your app does not conflict with python or django existing packages
-create a README.rst
-create a setup.py (please see django-polls folder)
-since only python modules are included the packages, create a MANIFEST.in file and specify there the additional files such
LICENSE, README.rst, static folder, and template folder
you may include as well the docs folder for possible future documentation

39 create the installer of your package by running this command inside of your installation folder mentioned above --> python setup.py sdist
-this will create another folder dist where a tar.gz file reside

40 you can now install your package by running --> pip install installer.tar.gz
