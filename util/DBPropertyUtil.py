import configparser

class DBPropertyUtil:
    @staticmethod
    def getPropertyString(filename):
        config = configparser.ConfigParser()
        config.read(filename)
        connection_string = f'DRIVER={{SQL Server}};SERVER=DESKTOP-MB0Q7BK;DATABASE=CARS;Trusted_Connection=True'
        return connection_string
