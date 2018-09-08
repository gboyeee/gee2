import gitlab, os, json, itertools
from pprint import pprint

def glab():
    return gitlab.Gitlab(
        os.environ['GITLAB_URL'],
        private_token=os.environ['GITLAB_TOKEN']
    )

def scan_requirements():
    files = ( (p.repository_raw_blob(f['id']).decode('utf-8').strip()
        for f in p.repository_tree() if f['name'] == 'requirements.txt')
            for p in glab().projects.list(all=True, as_list=False) )

    req_set = set()
    for contents in itertools.chain.from_iterable(files):
        req_set.update(contents.split("\n"))
    return req_set

if __name__ == '__main__':
    for e in scan_requirements():
        print(e)
