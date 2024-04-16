#!/bin/bash

/etc/init.d/cron restart && /etc/init.d/cron status && /etc/init.d/cron start && /usr/local/bin/uwsgi /app/uwsgi.ini