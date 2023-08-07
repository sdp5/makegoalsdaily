# make-goals-daily

#### Make contribution to your short term goals daily :)
##### And stay on track, just in 3 steps..

* enter short term goals
* log your activity daily
* leave rest to the app


### Deploy and Test

* Install and configure apache with mod_wsgi for py3
* Download or clone project and change to project dir
* Create virtualenv and RUN `make env` `make migrate` commands
* Setup apache conf as [makegoalsdaily.conf](deploy/apache/makegoalsdaily.conf)
* Set write permission for db.sqlite3 and RUN `python3 manage.py initlogin`


### Get Involved

* RUN `git clone https://github.com/sundeep-co-in/makegoalsdaily.git`
* Create a virtualenv and activate it.
* RUN `make env` `make migrate` `make initlogin` `make run` commands
* Point your browser to localhost:8000 and import project in your IDE
* Create GitHub [issues](https://github.com/sundeep-co-in/makegoalsdaily/issues) and lets discuss how we can make this better!

##### To run tests

* Download `geckodriver` from https://github.com/mozilla/geckodriver/releases
* Place it in `bin` directory of the virtual env.
* RUN `make test` command to execute tests.

### License

[MIT License](https://opensource.org/licenses/MIT)
