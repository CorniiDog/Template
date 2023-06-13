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
    This function is used to save objects to the databse folder

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