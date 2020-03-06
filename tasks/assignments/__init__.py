import __main__
import getpass


def show_assignment1(username=None):
    if not username:
        username = getpass.getuser()
    try:
        import requests
        resp = requests.post(f'https://python.lt/api/oop/1/get/{username}/')
        if resp.ok:
            print(resp.text)
        else:
            print(f'ERROR: could not retrieve Assignment Nr 1, because got {resp.status_code}, reason {resp.text}')

    except Exception as exc:
        print(f'ERROR: could not retrieve Assignment Nr 1, because {exc}')


def check_assignment1(username=None):
    if not username:
        username = getpass.getuser()
    try:
        import requests
        import json
        import base64
        import dill

        objects = {e: getattr(__main__, e) for e in dir(__main__)
                if not e.startswith('_') and
                e not in ['In', 'Out', 'exit', 'get_ipython', 'quit', 'check_assignment1', 'show_assignment1']}
        pickled_objects = base64.b64encode(dill.dumps(objects))

        resp = requests.post(f'https://python.lt/api/oop/1/check/{username}/', data={'objects': pickled_objects})

        if resp.ok:
            print(resp.text)
        else:
            print(f'ERROR: could not check Assignment Nr 1, because got {resp.status_code}, reason {resp.text}')

    except Exception as exc:
        print(f'ERROR: could not check Assignment Nr 1, because {exc}')


def show_assignment2(username=None):
    if not username:
        username = getpass.getuser()
    try:
        import requests
        resp = requests.post(f'https://python.lt/api/oop/2/get/{username}/')
        if resp.ok:
            print(resp.text)
        else:
            print(f'ERROR: could not retrieve Assignment Nr 2, because got {resp.status_code}, reason {resp.text}')

    except Exception as exc:
        print(f'ERROR: could not retrieve Assignment Nr 2, because {exc}')
