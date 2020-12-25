if [ "$ENVIROMENT" == "LOCAL" ];
then
    echo "NOT DEPLOYED ENVIROMENT. Access to the container and use django python manage.py runserver instead"
    echo "Keeping container alive..."
    while true; do sleep 1; done
else
    echo "Starting gunicorn server in DEPLOYED ENVIROMENT" 
    gunicorn --bind :8000 --workers 2 ${APP_NAME}.wsgi:application
fi
