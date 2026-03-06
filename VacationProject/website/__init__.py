from flask import Flask


def create_app():
    app = Flask (__name__)
    app.config['SECRET_KEY'] = 'whatever'

    from .country import country
    from .activity import activities
    from .city import city
    from .user import user
    from .vacation import vacation

    app.register_blueprint(country, url_prefix = "/")  #the startup page

    # hämtas enligt /blabla (vi kan lägga till)#
    app.register_blueprint(activities, url_prefix = "/activities")
    app.register_blueprint(city, url_prefix = "/city")
    app.register_blueprint(user, url_prefix = "/user")
    app.register_blueprint(vacation, url_prefix = "/vacation")


    return app