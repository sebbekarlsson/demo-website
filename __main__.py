from flask import Flask, request, jsonify
import git
import os

app = Flask(__name__)


def clone_repo_from_github(clone_url):
    print('Cloning {}'.format(clone_url))
    git.Git("/var/www").clone(clone_url)


def pull_repo_from_github(repo_path):
    print('Pulling {}'.format(repo_path))
    g = git.cmd.Git(repo_path)
    g.pull()

@app.route('/', methods=['POST', 'GET'])
def receive_data_from_github():
    data = request.json
    repo = data.get('repository', {})
    clone_url = repo.get('clone_url', None)
    name = repo.get('name', '')

    full_path = '/var/www/{}'.format(name)
    
    if os.path.isdir(full_path):
        pull_repo_from_github(full_path)
    elif clone_url:
        clone_repo_from_github(clone_url)

    return jsonify({ 'hej': 1 })

app.run(debug=True, host='178.62.44.12')
