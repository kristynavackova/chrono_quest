from waitress import serve
from chronoQuest import main

def create_app():
    return main()

if __name__ == '__main__':
    app = create_app()
    # 127.0.0.1 = dostupné jen z tvého počítače (bezpečné pro vývoj)
    serve(app, host='127.0.0.1', port=8000)
