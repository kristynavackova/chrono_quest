from pyramid.config import Configurator
import mimetypes


def main(global_config=None, **settings):
    # Add support for WebP images
    mimetypes.add_type('image/webp', '.webp', strict=True)

    # Disable template caching during development (to be removed in production)
    # Na pythonAnywhere.com není auto-reload šabllon potřeba.
    settings['pyramid.reload_templates'] = False

    # Create Pyramid WSGI application
    with Configurator(settings=settings) as config:
        config.include("pyramid_jinja2")
        # Statické soubory (CSS, JS, obrázky)
        config.add_static_view(name='static', path='chronoQuest:static', cache_max_age=86400)
        # Definice rout (URI) a jejich mapování na view funkce
        # The root URL redirects to /home
        config.add_route("root","/")
        config.add_route("home","/home")
        config.add_route('themes','/themes')
        config.add_route('login', '/login')
        config.add_route('signup', '/signup')
        # Dev endpoint pro testování e-mailů - smaž před nasazením do produkce!
        config.add_route("mail_test", "/__mailtest")
        config.scan('.views')
        app = config.make_wsgi_app()
    return app