class AuthRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    route_app_labels = {'auth', 'contenttypes','sessions','admin','users','clients'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to main.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'main'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to main.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'main'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'main' database.
        """
        if app_label in self.route_app_labels:
            return db == 'main'
        return None
    


class Client:
   
    route_app_labels = {'clients','auth', 'contenttypes','sessions','admin','users'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to clients.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'clients'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to clients.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'clients'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'clients' database.
        """
        if app_label in self.route_app_labels:
            return db == 'clients'
        return None


