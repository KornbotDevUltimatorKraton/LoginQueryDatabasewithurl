echo 'Installation for the heroku'
sudo snap install --classic heroku 
echo 'Access via the linux and get the link from the login output'
heroku login 
echo 'Heroku create app'
heroku create appname  #Getting the app name
echo 'Heroku addons create app'
heroku addons:create heroku-postgresql:hobby-dev -a appname #Getting the appname create the addons 
echo 'Get the DATABASE_URL from this command '
heroku config:get DATABASE_URL -a appname # Getting the heroku database link command to get the database app 
echo 'Now using the postgresql-namesession as database URL'
echo 'Next start coding on your code and connect the database'
  

