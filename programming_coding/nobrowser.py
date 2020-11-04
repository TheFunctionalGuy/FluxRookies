import requests

if __name__ == '__main__':
    response = requests.get('https://rkchals.fluxfingers.net/code/nobrowser.php')
    print(response.content)
