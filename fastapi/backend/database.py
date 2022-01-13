from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client['main']


class Database:

    @staticmethod
    def insert_tokens(item: dict):
        try:
            db.tokens.insert_one(item)  # insert_meny()
            return 'запись создана'
        except Exception as e:
            return f'ошибка: {e}'
        
    @staticmethod
    def replace_files(item1: dict, item2: dict):
        try:
            db.files.replace_one(item1, item2, True)
            return 'запись обновлена'
        except Exception as e:
            return f'ошибка: {e}'
    

    @staticmethod
    def find_all_files():
        try:
            return db.files.find()
        except Exception as e:
            pass

    @staticmethod
    def find_tokens(request: dict):
        try:
            return db.tokens.find_one(request)
        except Exception as e:
            return f'ошибка: {e}'
        
    @staticmethod
    def find_file(request: dict):
        try:
            return db.files.find_one(request)
        except Exception as e:
            return f'ошибка: {e}'

    @staticmethod
    def delete_token(request: dict):
        try:
            db.tokens.delete_one(request)
        except Exception as e:
            return f'ошибка: {e}'
