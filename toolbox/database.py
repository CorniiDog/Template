import os, pickle

storage_folder = os.path.join(os.path.dirname(__file__), 'database')
if not os.path.exists(storage_folder):
    os.makedirs(storage_folder)


def get(name: str) -> object:
    """
    Parameters
    ----------
    name : str
        The name of the file to be loaded

    Returns
    -------
    object
        The object loaded from the file, could be anything

    Notes
    -----
    This function is used to load objects from the database folder

    References
    ----------
    No Links

    Examples
    --------
    spreadsheet_data = get('spreadsheet_people')
    """
    if name.endswith('.pkl'):
        name = name[:-4]
    path = os.path.join(storage_folder, name + '.pkl')
    with open(path, 'rb') as f:
        return pickle.load(f)


def save(name: str, data: any) -> None:
    """
    Parameters
    ----------
    name : str
        The name of the file to be saved
    data : any
        The data to be saved

    Returns
    -------
    None
        This function does not return anything

    Notes
    -----
    This function is used to save objects to the database folder

    References
    ----------
    No Links

    Examples
    --------
    spreadsheet_data = {"People": ["Bill", "Kent", "Steve"], "Ages": [20, 30, 40]}

    save('spreadsheet_people', spreadsheet_data)
    """
    if name.endswith('.pkl'):
        name = name[:-4]
    path = os.path.join(storage_folder, name + '.pkl')
    with open(path, 'wb') as f:
        pickle.dump(data, f)

def delete_database(name: str) -> object:
    """
    Parameters
    ----------
    name : str
        The name of the file to be deleted

    Returns
    -------
    object
        The object loaded from the file, could be anything

    Notes
    -----
    This function is used to delete objects from the database folder

    References
    ----------
    No Links

    Examples
    --------
    spreadsheet_data = {"People": ["Bill", "Kent", "Steve"], "Ages": [20, 30, 40]}

    save('spreadsheet_people', spreadsheet_data)

    delete_database('spreadsheet_people')
    """

    if name.endswith('.pkl'):
        name = name[:-4]

    contents = get(name)
    path = os.path.join(storage_folder, name + '.pkl')
    os.remove(path)
    return contents

def save_key(platform: str, key: str, override: bool=False) -> None:
    """
    Parameters
    ----------
    platform: str
        The name of the platform to be saved (e.g. 'google')
    key: str
        The key to be saved (e.g. '<google_api_key>')

    Returns
    -------
    None
        This function does not return anything

    Notes
    -----
    This function is used to save keys in a secure location

    References
    ----------
    https://www.nylas.com/blog/making-use-of-environment-variables-in-python/

    Examples
    --------
    save_key('google', '<google_api_key>')
    """
    if not override:
        if platform in os.environ.keys():
            raise Exception(f'Key {platform} already exists')

    os.environ[platform] = key


def load_key(platform: str) -> str:
    """
        Parameters
        ----------
        key: str
            The key to be loaded (e.g. '<google_api_key>')

        Returns
        -------
        str or None
            This function returns the key if it exists, otherwise it returns None

        Notes
        -----
        This function is used to load keys from a secure location

        References
        ----------
        https://www.nylas.com/blog/making-use-of-environment-variables-in-python/

        Examples
        --------
        key = load_key('google')
        """
    if platform in os.environ.keys():
        return os.environ[platform]
    else:
        return None