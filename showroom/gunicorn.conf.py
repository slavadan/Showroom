bind = "127.0.0.1:8000"
workers = 1
errorlog = '/home/slavadan/whitesnake/Showroom/showroom/logs/gunicorn-error.log'
accesslog = '/home/slavadan/whitesnake/Showroom/showroom/logs/gunicorn-access.log'
wsgi_app = 'showroom.wsgi'
loglevel = 'debug'
