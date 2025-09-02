from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

@view_config(route_name='root')
def root_view(request):
    return HTTPFound(location=request.route_url('home'))


@view_config(route_name='home', renderer='chronoQuest:templates/home.jinja2')
def home_view(request):
    return {
        "title": "ChronoQuest - úvod",
        "themes": [
            {"year": 1, "name": "Uvězněni v čase"},
            {"year": 2, "name": "Útěk ze začarovaného světa"},
            {"year": 3, "name": "Boj o přežití"},
            {"year": 4, "name": "Hledání cesty domů"},
        ],
    }

@view_config(route_name='login', renderer='chronoQuest:templates/login.jinja2', request_method=('GET','POST'))
def login_view(request):
    # TODO: zde později zpracujeme POST (ověření uživatele, session, redirect)
    return {"title": "Přihlášení"}

@view_config(route_name='signup', renderer='chronoQuest:templates/signup.jinja2', request_method=('GET','POST'))
def signup_view(request):
    # TODO: zde později zpracujeme POST (vytvoření účtu)
    return {"title": "Registrace"}
