# MyPythonProject
Contains Django and other python code

Using Database in django:
------------------------------

Create Model in app ( classes which define columns and field types )
Run makemigrations - python manage.py makemigration music
Run migration 	   - python manage.py migrate
This will populate db.sqllite with necessary date

Flow - Hit the app --> goes to settings --> check Installed Apps --> Goes to apps --> Goes to model
==================================================================================================

Create Table in Database:
------------------------
1. Open Shell using python manage.py shell
2. Import our class - from music.models import Album, Song
3. Check for our object = Album.objects.all() - This will get nothing as there are no entries yet
4. Make an entry like in object like a = Album(artist="Priyanka Chopra", album_title="Exotic", genre="Pitbull", album_logo="https://upload.wikimedia.org/wikipedia/en/f/f1/Exotic-Single-Cover.jpg")
5. Save it to database from shell using a.save()
6. Now you can view object like a.artist and a.id

### Flask App
#### To create database
- From python terminal
```
>>> from app import db
>>> db.create_all()
>>>
```
- Add some dummy data from command line
```
>>> from app import User, Post
>>> user_1 = User(username='atishay', email='atishay@email.com', password='password')
Here id will be added automatically
image has default value
>>> db.session.add(user_1)
>>> user_2 = User(username='lokesh', email='lokesh@email.com', password='password')
>>> db.session.add(user_2)
>>> db.session.commit()
```

- Lets try to query our database. It is very easy with sql alchemy
```
User.query.all()
[User('atishay', 'atishay@email.com', 'default.jpg'), User('lokesh', 'lokesh@email.com', 'default.jpg')]
>>> User.query.first()
User('atishay', 'atishay@email.com', 'default.jpg')
>>> User.query.filter_by(username='atishay').all()
[User('atishay', 'atishay@email.com', 'default.jpg')]
```

- If we query post by user atishay it return empty list for now
```
>>> user = User.query.filter_by(username='atishay').first()
>>> user.id
1
>>> user.posts
[]
>>>
```
- We know posts is referencing the posts table
- Lets create some posts
```
>>> post_1 = Post(title='Blog 1', content='First Post Content!', user_id=user.id)
>>> post_2 = Post(title='Blog 2', content='Second Post Content!', user_id=user.id)
>>> db.session.add(post_1)
>>> db.session.add(post_2)
>>> db.session.commit()
```
- Lets query posts by user id 1 again
```
>>> user.posts
[User('Blog 1', '2020-10-18 17:09:27.926180'), User('Blog 2', '2020-10-18 17:09:27.928175')]
```
```
>>> for post in user.posts:
...   print(post.title)
...
Blog 1
Blog 2
>>>
```
- Lets get the user id from post
```
>>> post = Post.query.first()
>>> post
User('Blog 1', '2020-10-18 17:09:27.926180')
>>> post.user_id
1
>>>
```
- Lets see what backref do
Note here we do not have any column as author in the post with backref it is extremely easy
```
>>> post.author
User('atishay', 'atishay@email.com', 'default.jpg')
>>>
```

- Lets delete all the data to start fresh
```
>>> db.drop_all()
>>> db.create_all()
>>> User.query.all()
[]
>>> Post.query.all()
[]
>>>
```
### Actual creation of user and password
- Verify from db
```
from flaskapp import db
User.query.all()
from flaskapp.models import User
User.query.first()
User('atishay', 'atishay@email.com', 'default.jpg')
user = User.query.first()
user.password
'$2b$12$bVro9SQ6HZ1Yxs4EouceTebrE3BYEOc7.Eq/zddYdQdxt4lA7dWXi'
```
- It does not stop us from using the same user and password again until we save it in database
```
sqlalchemy.exc.IntegrityError
sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) UNIQUE constraint failed: user.email
[SQL: INSERT INTO user (username, email, image_file, password) VALUES (?, ?, ?, ?)]
[parameters: ('atishay', 'atishay@email.com', 'default.jpg', '$2b$12$7dDaHPt8J6GMWBOAwd6lFOQRaADCh6xErUVShsjstYGpV7zla1nPa')]
(Background on this error at: http://sqlalche.me/e/13/gkpj)
```
We solve this in forms by using flasks validators which are included in flask wtf


### Deployment

- We will use gunicorn and nginx for this
- Not recommended to use development server
```
sudo apt install nginx
```
- Install gunicorn in virtual env
```
pip install gunicorn
```
- nginx will be webserver and will be handling static file and other things
- Python stuff will be handled by gunicorn

#### Steps

1. Remove the default config file for nginx
```
sudo rm /etc/nginx/sites-enabled/default
```
2. Create a new one
```
sudo nano /etc/nginx/sites-enabled/flaskapp

server {
        listen 80;
        server_name 3.8.120.252;

        location /static {
                alias /home/atishay/MyPythonProject/flaskapp/static;
        }

        location / {
                proxy_pass http://localhost:8000;
                include /etc/nginx/proxy_params;
                proxy_redirect off;
        }
}
```

- Restart nginx

```
 sudo systemctl restart nginx
```

- Run gunicorn
```
gunicorn -w 3 run:app
```
- for number of workers gunicorn says (2 * num_cores) + 1
- no of cores = nproc --all

- But this is not we want as we want to restart gunicorn and run in background
- We will use supervisor for this
```
sudo apt install supervisor
```
```
sudo nano /etc/supervisor/conf.d/flaskapp.conf

[program:flaskapp]
directory=/home/atishay/MyPythonProject
command=/home/atishay/MyPythonProject/venv/bin/gunicorn -w 3 run:app
user=atishay
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
stderr_logfile=/var/log/flaskapp/flaskapp.err.log
stdout_logfile=/var/log/flaskapp/flaskapp.out.log
```
- Now create the log files
```
sudo mkdir -p /var/log/flaskapp
sudo touch /var/log/flaskapp/flaskapp.err.log
sudo touch /var/log/flaskapp/flaskapp.out.log
```

- Restart supervisor
```
(venv) atishay@flask-server:~/MyPythonProject$ sudo supervisorctl reload
Restarted supervisord
```
