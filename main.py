from bevyframe import *
from bevyframe.Features.Login import get_session
from dotenv import load_dotenv
import os


def get(r: Request) -> Response:
    return redirect('https://github.com/hereus-pbc/serverMainProc')


load_dotenv('./.env')
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
def get_session_route(r: Request, appname: str) -> Response:
    app_order = [
        'account',  # Redirect 1/18
        'search',   # Redirect 2/18
    ]
    current_index = app_order.index(appname)
    if current_index == len(app_order) - 1:
        resp = redirect('https://account.hereus.net/')
    else:
        next_app = app_order[current_index + 1]
        resp = redirect(f'https://{next_app}.hereus.net/get_session?token={r.cookies["s"]}')
    creds = get_session(app.secret, r.query['token'])
    resp.credentials = creds
    resp.body = creds['email']
    return resp


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=False
    )
