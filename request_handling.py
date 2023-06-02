import requests

url_followers = 'https://api.github.com/users/{}/followers'
url_following = 'https://api.github.com/users/{}/following'
url_id = 'https://api.github.com/users/{}'

gh_session = requests.Session()


def init_session(gh_username, gh_password):
    gh_session.auth = (gh_username, gh_password)

def get_user_followers(user):
    data = gh_session.get(url_followers.format(user))
    if data.status_code != 200:
        print("We're gonna have a problem here. Follower get failure with status code: [ {} ]".format(data.status_code))
        return
    follower_data = data.json()
    return follower_data

def get_user_following(user):
    data = gh_session.get(url_following.format(user))
    if data.status_code != 200:
        print("We're gonna have a problem here. following get failure with status code: [ {} ]".format(data.status_code))
        return
    following_data = data.json()
    return following_data

def get_user_id(user):
    data = requests.get(url_id.format(user))
    if data.status_code != 200:
        print("Error! Status: " + str(data.status_code))
        return
    id_data = data.json()
    return id_data['id']
    
