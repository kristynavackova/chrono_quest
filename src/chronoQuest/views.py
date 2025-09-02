from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from .services.mail_service import send_email, MailError
from pyramid.httpexceptions import HTTPBadRequest
import html


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
@view_config(route_name="mail_test", renderer="string", request_method="GET")
def mail_test(request):
    """
    DEV: /__mailtest?to=uzivatel@pslib.cz
    Pošli si testovací e-mail. Po nasazení do produkce tenhle endpoint smaž!
    """
    to = (request.params.get("to") or "").strip()
    if not to:
        # jednoduchá nápověda, ať víš, jak endpoint volat
        return "Použij /__mailtest?to=uzivatel@pslib.cz"

    # (volitelná) pojistka: povol jen školní doménu
    if not to.lower().endswith("@pslib.cz"):
        raise HTTPBadRequest("Pro test povolena jen doména @pslib.cz")

    app_url = request.application_url  # např. https://reviorion.pythonanywhere.com
    subject = "ChronoQuest – test e-mailu"
    body = f"""
    <div style="font-family:system-ui,Segoe UI,Roboto,Arial">
      <h2>Test e-mailu z ChronoQuest</h2>
      <p>Pokud tohle vidíš hezky naformátované, SMTP funguje ✅</p>
      <p>Base URL aplikace: <a href="{html.escape(app_url)}">{html.escape(app_url)}</a></p>
      <hr>
      <small>Tip: tenhle endpoint po ověření smaž nebo zařiď, aby byl jen v DEV.</small>
    </div>
    """
    try:
        send_email(to=to, subject=subject, html=body)
    except MailError as e:
        # vrátím čitelnou chybu do prohlížeče (bez tajemství)
        raise HTTPBadRequest(f"Odeslání selhalo: {e}")

    # jednoduché potvrzení
    return f"OK, posláno na {to}"