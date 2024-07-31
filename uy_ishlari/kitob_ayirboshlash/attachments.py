from jsonManager import attach_manager
from typing import Union


class Attachment:
    def __init__(self, full_name, phone, get, give):
        self.full_name = full_name
        self.phone = phone
        self.get = get
        self.give = give

    @staticmethod
    def find_attach(phone) -> Union[list, bool]:
        data = attach_manager.read()
        temp = []
        for attach in data:
            if attach['phone'] == phone:
                temp.append(attach)
        if temp:
            return temp
        else:
            return False
