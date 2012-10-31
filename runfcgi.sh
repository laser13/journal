#!/bin/bash

PROJDIR="/usr/local/www/django/journal"
PIDFILE="$PROJDIR/journal.pid"
SOCKET="$PROJDIR/journal.sock"

cd $PROJDIR
if [ -f $PIDFILE ]; then
    kill `cat -- $PIDFILE`
    rm -f -- $PIDFILE
fi

python manage.py runfcgi socket=$SOCKET method=prefork daemonize=true pidfile=$PIDFILE

chmod 0777 $SOCKET

echo 'Готово!'