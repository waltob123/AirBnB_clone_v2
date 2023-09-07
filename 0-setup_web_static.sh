#!/usr/bin/env bash
# a script that sets up your web servers for the deployment of web_static

# update and upgrade
apt-get update

# install nginx
apt-get install -y nginx

# create folders if it doesn't exist
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# create a fake html file with simple content
echo "<h1>Hello, Welcome to ALX!</h1>" > /data/web_static/releases/test/index.html

# create a symbolic link between two files (directories)
ln -s -f /data/web_static/releases/test/ /data/web_static/current

# change ownership of data directory (including its child elements)
chown -R ubuntu:ubuntu /data/

# update nginx configuration file
printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

# restart nginx server
service nginx restart

