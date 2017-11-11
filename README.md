# malochertool

Eine Webapp geschrieben in Python mit dem Framework Flask.

Es können Arbeitseinsaätze verwaltet und Anträge automatisch generiert werden.

Dient auch als Testprojekt, um zu sehen, ob man die NAJU App in Python schreiben könnte.

Es muss eine private config angelegt werden. Im Hauptordner einen Ordner `instance` erstellen.
Darin eine Datei `flask.cfg` erstellen mit dem Inhalt

    import os
    
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    TOP_LEVEL_DIR = os.path.abspath(os.curdir)
    
    SECRET_KEY = 'My very private and secret key with 24 digits'
    DEBUG = True
