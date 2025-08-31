class AppSettings:
    __instance = None # private class-level variable

    def __init__(self):
        if AppSettings.__instance is not None:
            raise RuntimeError("Use get_instance() instead of direct instantiation")
        self.database_url = "localhost:5432"
        self.api_key = "1234-ABCDE"
        AppSettings.__instance = self

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = AppSettings()
        return cls.__instance
        
    def get_database_url(self):
        return self.database_url
    
    def get_api_key(self):
        return self.api_key
    
class WithSingletonPattern:
    def main(self):
        app_settings_v1: AppSettings = AppSettings.get_instance()
        app_settings_v2: AppSettings = AppSettings.get_instance()

        print(app_settings_v1.get_api_key())
        print(app_settings_v2.get_api_key())

        # Are the two objects same?
        # Ans: No
        print(app_settings_v1 == app_settings_v2)
        print(app_settings_v1 is app_settings_v2)

if __name__ == "__main__":
    obj: WithSingletonPattern = WithSingletonPattern()
    obj.main()
