import os


def url_path():
    """
        Prompts the user to enter a URL and a path as strings via the terminal.

        --------
        Returns:
        url: str
            The URL entered by the user.
        path: str
            The path entered by the user.
        --------
    """

    # for the path
    special_characters = "!@#$%^&*-+?=,<>"

    print(f'\nWelcome to the Unzipper 3000!')
    print(f'\nFirst, please define the path of the working directory.')
    print(f'Here is an example path for Windows: "C:/folder_name/"')
    print("---------------------------------------------")
    print(f'Note that special characters such as {special_characters} are not allowed in the path name.\n')
    print(f'Type or copy the entire path to the working directory in the terminal/prompt. \n')
    print("---------------------------------------------")

    # path input from user
    path = input("Now let us begin! Enter the folder path here: ")

    # check if the path already exists
    if any(spec in special_characters for spec in path):
        print(f'This path contains special character(s). Please give a new path: \n')
        while any(scpec in special_characters for scpec in path):
            path = input()
            if os.path.exists(path):
                print(f'Great! This working directory is valid. \n')
            # if the path not exists
            else:
                if not os.path.exists(path):
                    try:
                        os.makedirs(os.path.dirname(path))
                        print(f'New working directory is now created.')
                    except FileExistsError:
                        print(f'This working directory already exists.')

    else:
        if os.path.exists(path):
            print(f'Great! This working directory is valid. \n')
        else:
            if not os.path.exists(path):
                try:
                    os.makedirs(os.path.dirname(path))
                    print(f'New working directory is now created.')
                except FileExistsError:
                    print(f'This working directory already exists.')

    # for the URL
    print(f'\nNow please define the URL from which the data will be downloaded!')
    print(f'The URL must end on ".zip", otherwise your data can not be extracted. \n')

    # URL input from user
    url = input("Now enter the URL here: ")

    return url, path
