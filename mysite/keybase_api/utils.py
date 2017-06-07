import requests


def request_keybase_user(keybase_login):

    keybase_user_api_url = (
            'https://keybase.io/_/api/1.0/user/lookup.json?usernames={keybase_login}&fields=basics,public_keys'
    )
    keybase_user_data = requests.get(keybase_user_api_url.format(
        login=keybase_login,
    )
    )
    all_data_user = keybase_user_data.json()
    them_data = all_data_user['them']
    basic_data_list = them_data[0]
    basic_with_name = basic_data_list['basics']
    key_data = basic_data_list['public_keys']
    key_spec_data = key_data['primary']

    return {
        'login': basic_with_name['username'],
        'public_key': key_spec_data['bundle'],
    }
