from bevyframe import *
from bevyframe.Features.Login import get_session
from dotenv import load_dotenv
import os


def get(r: Request) -> Response:
    return redirect('https://github.com/hereus-pbc/serverMainProc')


app = Frame(
    package='net.hereus',
    developer='hereus@hereus.net',
    administrator=False,
    secret=os.environ.get('SECRET'),
    style="./HereUS-UI-3.1/HereUS-UI-3.1.json",
    icon="https://www.hereus.net/static/favicon.png",
    keywords=["search", "theprotocols", "decentralized"],
    default_network="hereus.net",
)


@app.route('/<appname>/src/get_session')
def get_session(r: Request) -> Response:
    app_order = [
        'search',  # Redirect 2/18
    ]
    current_index = app_order.index(r.query['token'])
    if current_index == len(app_order) - 1:
        return redirect('https://account.hereus.net/')
    else:
        next_app = app_order[current_index + 1]
        creds = get_session(app.secret, r.query['token'])
        resp = redirect(f'https://{next_app}.hereus.net/get_session?token={r.cookies["s"]}')
        resp.credentials = creds
        return resp



if __name__ == '__main__':
    load_dotenv('./.env')
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True
    )
