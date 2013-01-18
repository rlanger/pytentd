"""Default arguments for tentd"""

# Place the database in the current directory
MONGODB_SETTINGS = {
    'db': 'tentd',
}

# The name of the pidfile used by the daemon mode
PIDFILE = "/var/run/pytentd.pid"

# Run threaded. This shoud be disabled if deployed through WSGI.
THREADED = True
