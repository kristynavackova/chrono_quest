from pyramid.view import view_config


@view_config(route_name='home', renderer='C:\\Users\\Martin\\Desktop\\ŠR 25-26\\Tools\\ChronoQuest\\chrono_quest\\src\\chronoQuest\\templates\\home.jinja2')
def home_view(request):
    return {
        "title": "ChronoQuest - úvod",
        "themes": [
            {"year": 2025, "name": "Cyberpunk metropole"},
            {"year": 2026, "name": "Steampunk kolonie"},
            {"year": 2027, "name": "Biotech prales"},
        ],
    }

@view_config(route_name='themes', renderer='json')
def themes_api(request):
    return{
      "themes": [
            {"year": 2025, "slug": "cyberpunk", "name": "Cyberpunk metropole"},
            {"year": 2026, "slug": "steampunk", "name": "Steampunk kolonie"},
            {"year": 2027, "slug": "biotech", "name": "Biotech prales"},
        ]  
    }

@view_config(route_name='ping', renderer='string')
def ping_view(request):
    return 'pong'
