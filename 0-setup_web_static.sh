#!/usr/bin/env bash
apt-get update

apt-get install -y nginx
sudo ufw allow 'Nginx HTTP'

mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

echo "<html>
<head>
</head>
<body>
Holberton School
</body>
</html>
" > /data/web_static/releases/test/index.html

ln -s /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

sed -i '57i\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-enabled/default

service nginx restart

