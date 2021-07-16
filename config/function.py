import json


async def check_balance(user: str):
    with open('json/users.json', 'r') as f:
        users = json.load(f)

    user = str(user)
    return users[user]['balance']

async def add_balance(user: str, bal: int):
    with open('json/users.json', 'r') as f:
        users = json.load(f)

    user = str(user)
    users[user]['balance'] += bal

    with open('json/users.json', 'w') as f:
        json.dump(users, f)

async def remove_balance(user: str, bal: int):
    with open('json/users.json', 'r') as f:
        users = json.load(f)
    user = str(user)
    if(users[user]['balance'] - abs(bal)) < 0:
        return False

    with open('json/users.json', 'r') as f:
        json.dump(users, f)

    return True



async def update_data(users, user):
    if not str(user.id) in users:
        _id = str(user.id)
        users[_id] = {}
        users[_id]['experience'] = 0
        users[_id]['level'] = 1
        users[_id]['balance'] = 20

async def add_experience(users, user, exp):
    users[str(user.id)]['experience'] += exp

async def level_up(users, user, channel):
    _id = str(user.id)
    experience = users[_id]['experience']
    lvl_start = users[_id]['level']
    lvl_end = int(experience ** (1/4))
    if lvl_start < lvl_end:
        await channel.send('{} has leveled up to level {}'.format(user.mention, lvl_end))
        users[_id]['level'] = lvl_end

