Provisioning a new site
=======================

##Requirements
* nginx
* Python3
* Git
* pip 3
* virtualenv

eg. on Ubuntu
    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv

##Nginx Virtual Host configuration
* see nginx.template.conf
* replace SITENAME with url, eg: staging.my-domain.com

##Upstart Job
* see gunicorn-upstart.template.conf
* replace SITENAME with url, eg. staging.my-domain.com

##Folder structure
Assume we have an user account at /home/username

/home/username
|__ sites
    |__ SITENAME
         |-- database
	 |-- source
	 |-- static
	 |-- virtualenv



TTD with Python, p. 154
