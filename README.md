# orapi_cluster
Cluster on orangePI zero

INFORMATION

INSTALLATION

1. Install web server NGINX

apt install nginx

2. Make symlink for forlder

ln -s `pwd`/server/ /var/www/html/








SOME HELPERS

1. Get status about system:

/etc/update-motd.d/30-orangepi-sysinfo

2. WIFI ststus

iwconfig wlan0 retry
dhclient wlan0

/etc/resolv.conf
nameserver 77.88.8.8 # yandex dns

or

echo "nameserver 77.88.8.8 # yandex dns" >> /etc/resolv.conf


3. GIT commands

https://htmlacademy.ru/blog/git/git-console

git add .
git commit -m "some text of changes"
git push orign main

4. uth for GITHub

https://htmlacademy.ru/blog/git/git-console



