import app

wsgi = app.create_app()
wsgi.run(debug=True)
