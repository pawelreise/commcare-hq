CommCare HQ
===========

CommCare HQ is a server-side tool to help manage community health workers.
It seamlessly integrates with CommCare mobile and CommCare ODK, as well as
providing generic domain management and form data-collection functionality.

### Key Components

+ CommCare application builder
+ OpenRosa compliant xForms designer
+ SMS integration
+ Domain/user/CHW management
+ Xforms data collection
+ Case management
+ Over-the-air (ota) restore of user and cases
+ Integrated web and email reporting


Installing CommCare HQ
----------------------

Please note that these instructions are targeted toward UNIX-based systems.

### Installing dependencies

For Ubuntu 12.04, you can use the included `install.sh` script to install all
dependencies, set them up to run at startup, and set up required databases.
Then skip to "Setting up a virtualenv". 

Otherwise, install the following software from your OS package manager or the
individual project sites when necessary.

+ Python 2.6 or 2.7
+ pip
+ CouchDB >= 1.0 (1.2 recommended) ([installation instructions][couchdb])
+ PostgreSQL >= 8.4 - (install from OS package manager or [here][postgres])
+ [elasticsearch][elasticsearch] (including Java 7)
+ memcached
+ [Jython][jython] 2.5.2 (optional, only needed for CloudCare)
+ For additional requirements necessary only if you want to modify the default
  JavaScript or CSS styling, see [CommCare HQ Style](https://github.com/dimagi/hqstyle-src).

 [couchdb]: http://wiki.apache.org/couchdb/Installation
 [postgres]: http://jython.org/downloads.html
 [elasticsearch]: http://www.elasticsearch.org/download/
 [jython]: http://jython.org/downloads.html



#### Common issues

+ A bug in psycopg 2.4.1 (a Python package we require) may break CommCare HQ
  when using a virtualenv created with `--no-site-packages` or when the
  `egenix-mx-base` Python package is not already installed. To fix this, install
  `egenix-mx-base` (`sudo apt-get install python-egenix-mxdatetime` on Ubuntu)
  and use `virtualenv --with-site-packages` instead.

+ On Mac OS X, pip doesn't install the `libmagic` dependency for `python-magic`
  properly. To fix this, run `brew install libmagic`.

+ To install PIL (Python Image Library) correctly on Ubuntu, you may need to
  follow [these instructions](http://obroll.com/install-python-pil-python-image-library-on-ubuntu-11-10-oneiric/).

#### Configuration for Elasticsearch

To run elasticsearch in an upstart configuration, see [this example](https://gist.github.com/3961323).

To secure elasticsearch, we recommend setting the listen port to localhost on a
local machine. On a distributed environment, we recommend setting up ssh
tunneled ports for the elasticsearch port. The supervisor_elasticsearch.conf
supervisor config demonstrates the tunnel creation using autossh.


### Setting up a virtualenv

A virtualenv is not required, but it may make your life easier.

    sudo pip install virtualenv
    mkdir ~/.virtualenvs/
    virtualenv ~/.virtualenvs/commcare-hq --no-site-packages

### Downloading and configuring CommCare HQ

Once all the dependencies are in order, please do the following:

    git clone git@github.com:dimagi/commcare-hq.git
    cd commcare-hq
    git submodule update --init --recursive
    source ~/.virtualenvs/commcare-hq/bin/activate      # enter your virtualenv if you have one
    pip install -r requirements/requirements.txt -r requirements/prod-requirements.txt
    cp localsettings.example.py localsettings.py

Then, edit localsettings.py and ensure that your Postgres, CouchDB, email, and
log file settings are correct, as well as any settings required by any other
functionality you want to use, such as SMS sending and Google Analytics.

Ensure that the directories for `LOG_FILE` and `DJANGO_LOG_FILE` exist and are
writeable.

### Set up your django environment

    ./manage.py syncdb
    ./manage.py migrate
    ./manage.py collectstatic

    # this will do some basic setup, create a superuser, and create a project
    ./manage.py bootstrap <project-name> <email> <password>


Running CommCare HQ
-------------------

If your installation didn't set up the helper processes required by CommCare HQ
to automatically run on system startup, you need to run them manually:

    memcached -d &
    /path/to/unzipped/elasticsearch/bin/elasticsearch &
    /path/to/couchdb/bin/couchdb &

Our own helper processes must also be running:

    # Asynchronous task scheduler
    ./manage.py celeryd --verbosity=2 --beat --statedb=celery --events &

    # Keeps elasticsearch index in sync
    ./manage.py run_ptop &

    # only necessary if you want to use CloudCare
    jython submodules/touchforms-src/touchforms/backend/xformserver.py &

Finally, run HQ with

    ./manage.py run_gunicorn --workers=3

Or, for debugging:

    ./manage.py runserver --werkzeug


Building CommCare Mobile Apps
-----------------------------

In order to build and download a CommCare mobile app from your instance of
CommCare HQ, you need to follow our [instructions][builds] for how to download
and load CommCare binaries from the Dimagi build server.

 [builds]: https://github.com/dimagi/core-hq/blob/master/corehq/apps/builds/README.md
