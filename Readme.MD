# Application tracker
Application Tracker is an online database application to keep track of application that
you have applied to. There also is a suggestion in which someone could suggest a place
to apply at under the 'Suggestions' tab. To add applications you will need to log in.

# Installation

These are instructions to deploy onto an Amazon EC2 server

*What is required*
AWS Account - If you do not have one, you can sign up for a 12 month trail. This
configuration is set up to take the minimal costs if you are no longer in the trial
period.

1. After you log in go to EC2, and Launch a new instance.

## EC2 Configuration
1. SELECT AMI > Select Ubuntu Server
2. SELECT INSTNANCE TYPE > Select the t2.micro instance type. This is all you will need to run this app
3. CONGIGURE INSTNANCE > You do not really need to make any changes here.  
4. ADD STORAGE > You don't really need to make any changes here. This app is small and is not designed to take up that much space.
5. ADD TAGS > For convenience use the TAG NAME "App Tracker Server". This will be helpful to know what EC2 Instance is which if you use more than one. AWS will give you a warning about leaving SSH port open to the world.
6. CONFIGURE SECURITY GROUP > Create a new one if you do not have one open. Use the ports of SSH and HTML.
7. REVIEW > Create a new PGP key and it should download.

This Installation is not being designed to have good security. If you want to increase the security of
the site, I suggest that you learn more about Linux configuration or perhaps take some A Cloud Guru [courses](http://acloud.guru). These course are intended to give you more information about the AWS console, and help you prepare for an AWS certification. These courses are worth it. I suggest that you pay attention to [Udemy](http://www.udemy.com/) for when they are having a sale that reduces the courses to $10. These are the same courses that are on the A Cloud Guru site.

1. In your home directory create a directory called .ssh if you do not have one already.
2. Move the PEM file that was downloaded into the .ssh directory.
3. In the .ssh directory change the permission of the PEM file `chmod 600 `
4. Look at the EC2 console for the IP ADDRESS. Take note of this and the DNS. You will need these to configure the Apache client.
5. Connect to the newly created EC2 Instance once it is finished loading.
```
ssh -i ~/.ssh/FILENAME.pem ubuntu@IP_ADDRESS
```
Type Yes to create a fingerprint

Since this is the first time connecting, you will need to update the server:
```
$ sudo apt-get upgrade | y && sudo apt-get upgrade | y
```
You will then need to start to get the necessary packages need to run the Python applicaion:

```
$ sudo apt-get install apache2 postgresql python-pip python-dev build-essential git-all ntp python-psycopg2 libpq-dev libapache2-mod-wsgi python-virtualenv unattended-upgrades npm
```

Change directory to the www directory and clone the git repository:

```
$ cd /var/www
/var/www $ git clone https://github.com/jpdesigns316/Application-Tracker.git app-tracker
```

 Change into the app-tracker directory. Here you will need to configure some things.


Edit the Apache2 configuration file using nano, or the chosen editor of choice.
 ```
 /var/www/app-tracker $ sudo nano app-tracker.conf
 ```

Modify IP_ADDRESS with the IP address from the EC2 console;
Modify DNS ADDRSS with the DNS from the EC2 console.
Modify EMAIL with your email ADDRESS

Save the file and copy it into the apache directory, activate the conf file and restart.
```
/var/www/app-tracker $ sudo cp /etc/apache2/sites-available
/var/www/app-tracker $ sudo a2ensite app-tracker
/var/www/app-tracker $ sudo service apache2 restart
```

Now you will need to set up the PostgreSQL Database before you can start using the site.
```
$ sudo su PostgreSQL
```
Afer you are logged in, you will need to set up the tracker, and create the database.
```
createuser -interactive
```
Create the usernanme tracker, N to super user, Y to create database, N to create roles

Create the database
```
$ psql
```
Run these commands:
```
CREATE DATABASE apply OWNER tracker;
ALTER ROLE tracker WITH PASSWORD [choose what password you want];
```

Type CTRL-D twice to exit PostgreSQL console, then logout of Postgres account.

Make these modifications to the config.py in the app directory.

1. Comment out the section on the SQLite lines, and uncomment out the PostgreSQL lines.
2. Change the password that is listed for the variable PASSWORD
3. set SQLUSER to 'tracker', SQLPASSWORD to the one you set up in the Postgres section.

After making these modifications you should be ready for the final two steps.
Install the python modules without using the virtual environment. It is not needed
since this setup is minimal, and the server is only being used for this applicaiton.
```
pip install > requirements.txt
```
Create the models
```
/var/www/app-tracker/app $ python models.py
```

Everything **should** be configured to run site. Connect to it on your WWW client:
```
http://IP_ADDRESS/app_tracker
```

TODO:
1. Create a way to search applications by dates.
2. Increase the models to include setting up for locations by city or state so you can search by state
