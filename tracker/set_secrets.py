import json


def _set_secret(search_term, secrets_file='./tracker/secrets.json'):
    """
    Gets a secret from a  JSON file.
    File needs to be located in same directory. Example JSON below.
    {
        "key" : "[YOUR-KEY]"
    }
    :args:
        secrets_file: Optional path to secrets file. Default is current dir name: secrets.json
        search_term = A string to search the JSON file for
    Returns:
        Returns the secret found in the JSON file.
        If key is not present or fails returns -1
    """
    with open(secrets_file, encoding='utf-8') as secrets_file:
        secrets = json.load(secrets_file)
    try:
        return secrets[search_term]
    except:
        return -1
