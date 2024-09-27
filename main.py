# система управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень
# доступа и могут добавлять или удалять пользователя из системы.
#
# Требования:
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе:
# ID, имя и уровень доступа ('user' для обычных сотрудников).
# 2.Класс `Admin`: Этот класс должен наследоваться от класса `User`.
# Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
# Класс должен также содержать методы `add_user` и `remove_user`, которые позволяют
# добавлять и удалять пользователей из списка (представь, что это просто список экземпляров `User`).
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации
# снаружи. Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).

class User:

    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level


class Admin(User):

    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'

    def get_admin_access_level(self):
        return self._access_level

    def add_user(self, user):
        user_list.append(user)
        print(f"Добавлен пользователь {user.get_name()} с ID={user.get_user_id()} с правом доступа '{user.get_access_level()}'")

    def remove_user(self, user):
        user_list.remove(user)
        print(f"Удален пользователь {user.get_name()} с ID {user.get_user_id()}")

# Создание объектов пользователей
user1 = User(1, 'Иванов')
user2 = User(2, 'Петров')
user3 = User(3, 'Сидоров')

user_list = []

# Создание объекта администратора
admin = Admin(0, 'Администратор')

# Добавление и удаление пользователей администратором
admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)
admin.remove_user(user3)

for obj in user_list:
    print(obj._name)
