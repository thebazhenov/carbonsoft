
import argparse
import requests

def get_version():
    parser = argparse.ArgumentParser(
    prog='Получаем последнюю версию для .env по ветке',
    description='Import comments and attachments',
    epilog='RRRAAAAAMMMMM!')
    parser.add_argument('branch', default='devel')
    args = parser.parse_args()
    url = 'https://docker-registry.evateam.ru/v2/evateam/tags/list'
    res = requests.get(url).json()
    branch_version = [tag for tag in res['tags'] if tag.endswith(args.branch)]
    branch_version.sort()
    print(branch_version[-1])

if __name__ == "__main__":
    get_version()
