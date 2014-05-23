from fabric.api import local


# Local Development

def run_local_server(port=8000, debug=False):
    """ Runs just the local server, no migrations, db syncing, or PIP Install. """
    if debug:
        local("python manage.py runserver_plus %s --settings=settings.local" % port)
    else:
        local("python manage.py runserver %s --settings=settings.local" % port)

def run_local():
    """ PIP Installs, Syncs db, migrates, and runs a local django server. """
    pip_install_req('local')
    sync_db('local')
    migrate('local')
    run_local_server()
