# log-today

#### Make contribution to your short term goals daily :)
##### And stay on track, just in 3 steps..

* enter short term goals
* log your activity daily
* leave rest to the app


### Deploy and Test

##### Method 1

* Install and configure apache with mod_wsgi for py3
* Download or clone project and change to project dir
* Create virtualenv and RUN `make env` `make migrate` commands
* Setup apache conf as [makegoalsdaily.conf](deploy/apache/makegoalsdaily.conf)
* Set write permission for db.sqlite3 and RUN `python3 manage.py initlogin`

##### Method 2

* Setup docker on your machine
* RUN `docker pull suanand/makegoalsdaily` *(docker.io)*
* RUN `docker run -d --name appcontainer -p 8000:8080 suanand/makegoalsdaily`
* Point your browser to localhost:8000
* Login with admin and makegoalsdaily as password. Change password immediately.


### Get Involved

* RUN `git clone https://github.com/sundeep-co-in/logtoday.git`
* Create a virtualenv and activate it.
* RUN `make env` `make migrate` `make initlogin` `make run` commands
* Point your browser to localhost:8000 and import project in your IDE
* Create GitHub [issues](https://github.com/sundeep-co-in/makegoalsdaily/issues) and lets discuss how we can make this better!

### License

[MIT License](https://opensource.org/licenses/MIT)
