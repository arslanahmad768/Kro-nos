# K&R #

## General Information ##

This is REST API for the backend that powers [KROnos](https://kro-nos.com) application.

## Dependencies ##

Take a look at *requirements.txt* for Python dependencies, install and configure `redis-server` to listen to port 6379

## Installation ##

Copy the code to `/var/www/kandr`

Create virtual environment for the Python3 and install dependencies from `requirements.txt`, copy
`kandr-celery.service` and `kandr-gunicorn.service` to `/etc/systemd/system`, copy `backend.conf` to `nginx` vhost path,


Create SSL certificate using `certbot` for the FQDN of the backend and frontend host applications. As visible in the
`backend.conf`, create *symlink* for the newly created certificates and the key at `/etc/ssl/certs/kronos-web-cert.pem`
and `/etc/ssl/private/kronos-web-key.pem` respectively or modify the `backend.conf` file with appropriate paths for the
key and certificate.

Create and setup Postgresql database using `kandr`, `kandr` and `kandr` for host, database and password respectively, or
feel free to alter the `settings/production.py` with appropriate values for database settings followed by the
application of Django migrations.

Start the `nginx`, `kandr-gunicorn.service` and `kandr-celery.service` services.
