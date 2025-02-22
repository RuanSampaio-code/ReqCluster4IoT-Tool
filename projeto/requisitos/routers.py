# requisitos/routers.py

class MongoDBRouter:
    """
    Roteia o modelo Requisito para o MongoDB.
    """
    def db_for_read(self, model, **hints):
        if model._meta.model_name == 'requisito':
            return 'mongodb'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.model_name == 'requisito':
            return 'mongodb'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return None  # Não permitir relações entre bancos diferentes

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name == 'requisito':
            return db == 'mongodb'
        return db == 'default'