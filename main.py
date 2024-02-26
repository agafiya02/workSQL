from data import session
from data import users

users_info = [['Davis', 'Miller', 'Cooper'], ['John', "Albert", "Owen"], ['72', '61', '50'],
              ['colonist', 'colonist', 'colonist'], ['research engineer', 'research engineer', 'research engineer'],
              ['module_1', 'module_1', 'module_1'],
              ['1@mars.org', '2@mars.org', '3@mars.org']]


def main():
    session.global_init("db/users.db")
    db_session = session.create_session()
    user = users.User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"

    user1 = users.User()
    user1.surname = users_info[0][0]
    user1.name = users_info[1][0]
    user1.age = users_info[2][0]
    user1.position = users_info[3][0]
    user1.speciality = users_info[4][0]
    user1.address = users_info[5][0]
    user1.email = users_info[6][0]

    user2 = users.User()
    user2.surname = users_info[0][1]
    user2.name = users_info[1][1]
    user2.age = users_info[2][1]
    user2.position = users_info[3][1]
    user2.speciality = users_info[4][1]
    user2.address = users_info[5][1]
    user2.email = users_info[6][1]

    user3 = users.User()
    user3.surname = users_info[0][2]
    user3.name = users_info[1][2]
    user3.age = users_info[2][2]
    user3.position = users_info[3][2]
    user3.speciality = users_info[4][2]
    user3.address = users_info[5][2]
    user3.email = users_info[6][2]

    db_session.add(user)
    db_session.add(user1)
    db_session.add(user2)
    db_session.add(user3)
    db_session.commit()


if __name__ == '__main__':
    main()
