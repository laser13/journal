#!/bin/bash

PROJDIR="/usr/local/www/django/journal"
PIDFILE="$PROJDIR//nginx/journal.pid"
SOCKET="$PROJDIR/nginx/journal.sock"

cd $PROJDIR
if [ -f $PIDFILE ]; then
    kill `cat -- $PIDFILE`
    rm -f -- $PIDFILE
fi

source /home/laser13/virtualenvs/journal/bin/activate
python manage.py runfcgi socket=$SOCKET pidfile=$PIDFILE method=prefork daemonize=true
chmod 0777 $SOCKET

echo 'Готово!'