class AppSettings:
    def __init__(self):
        self.database_url = "localhost:5432"
        self.api_key = "1234-ABCDE"
        
    def get_database_url(self):
        return self.database_url
    
    def get_api_key(self):
        return self.api_key
    
class WithoutSingletonPattern:
    def main(self):
        app_settings_v1: AppSettings = AppSettings()
        app_settings_v2: AppSettings = AppSettings()

        print(app_settings_v1.get_api_key())
        print(app_settings_v2.get_api_key())

        # Are the two objects same?
        # Ans: No
        print(app_settings_v1 == app_settings_v2)
        print(app_settings_v1 is app_settings_v2)

if __name__ == "__main__":
    obj: WithoutSingletonPattern = WithoutSingletonPattern()
    obj.main()
