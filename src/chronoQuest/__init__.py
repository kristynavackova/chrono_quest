from pyramid.config import Configurator

def main(global_config=None, **settings):
    with Configurator(settings=settings) as config:
        config.include("pyramid_jinja2")
        config.add_route("home","/home")
        config.add_route('themes','/themes')
        config.add_route('ping', '/ping')
        config.scan('.views')
        app = config.make_wsgi_app()
    return app