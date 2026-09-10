from .base import MariaDBIdentifierPreparer as MariaDBIdentifierPreparer, MySQLDialect as MySQLDialect

class MariaDBDialect(MySQLDialect):
    is_mariadb: bool
    supports_statement_cache: bool
    name: str
    preparer = MariaDBIdentifierPreparer

def loader(driver): ...
