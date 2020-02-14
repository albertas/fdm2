import getpass
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
