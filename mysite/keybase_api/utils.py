import requests


def request_keybase_user(keybase_login):

    keybase_user_data = requests.get(
        'https://keybase.io/_/api/1.0/user/lookup.json?usernames={}&fields=basics,public_keys'
        .format(keybase_login))

    all_data_user = keybase_user_data.json()
    them_data = all_data_user['them']
    basic_data_list = them_data[0]
    basic_with_name = basic_data_list['basics']
    key_data = basic_data_list['public_keys']
    key_spec_data = key_data['primary']

    # PGP key from Keybase
    public_key = key_spec_data['bundle']
    # Nickname on Keybase
    login = basic_with_name['username']

    return {
        'login': login,
        'public_key': public_key,
    }