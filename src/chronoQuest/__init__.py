from pyramid.config import Configurator
import mimetypes


def main(global_config=None, **settings):
    mimetypes.add_type('image/webp', '.webp', strict=True)
    with Configurator(settings=settings) as config:
        config.include("pyramid_jinja2")
        config.add_static_view(name='static', path='chronoQuest:static', cache_max_age=0)
        config.add_route("home","/home")
        config.add_route('themes','/themes')
        config.add_route('login', '/login')
        config.add_route('signup', '/signup')
        config.scan('.views')
        app = config.make_wsgi_app()
    return app