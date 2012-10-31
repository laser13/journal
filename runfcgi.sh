#!/bin/bash

source /home/laser13/virtualenvs/journal/bin/activate

PROJDIR="/usr/local/www/django/journal"
PIDFILE="$PROJDIR/journal.pid"
SOCKET="$PROJDIR/journal.sock"

cd $PROJDIR
if [ -f $PIDFILE ]; then
    kill `cat -- $PIDFILE`
    rm -f -- $PIDFILE
fi

python manage.py runfcgi socket=$SOCKET pidfile=$PIDFILE method=prefork daemonize=true

chmod 0777 $SOCKET

echo 'Готово!'