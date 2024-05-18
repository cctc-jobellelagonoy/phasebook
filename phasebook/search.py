from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    id_results = []
    name_results = []
    age_results = []
    occupation_results = []

    for user in USERS:
        if 'id' in args and user['id'] == args['id']:
            id_results.append(user)
        if 'name' in args and args['name'].lower() in user['name'].lower():
            name_results.append(user)
        if 'age' in args and int(args['age']) - 1 <= user['age'] <= int(args['age']) + 1:
            age_results.append(user)
        if 'occupation' in args and args['occupation'].lower() in user['occupation'].lower():
            occupation_results.append(user)

    results = id_results + name_results + age_results + occupation_results
    results = list({v['id']:v for v in results}.values())

    return results