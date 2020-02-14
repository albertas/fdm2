import __main__
import getpass
import pickle

username = getpass.getuser()


def show_assignment1():
    try:
        import requests
        resp = requests.get(f'http://python.lt/api/oop/1/get/{username}/')
        if resp.ok:
            print(resp.text)
        else:
            print(f'ERROR: could not retrieve Assignment Nr 1, because got {resp.status_code}, reason {resp.text}')

    except Exception as exc:
        print(f'ERROR: could not retrieve Assignment Nr 1, because {exc}')


def check_assignment1():
    try:
        import requests
        resp = requests.post(f'http://python.lt/api/oop/1/check/{username}/', data={'objects': pickle.dumps(__main__)})

        if resp.ok:
            print(resp.text)
        else:
            print(f'ERROR: could not check Assignment Nr 1, because got {resp.status_code}, reason {resp.text}')

    except Exception as exc:
        print(f'ERROR: could not check Assignment Nr 1, because {exc}')
