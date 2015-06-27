from opbeat.instrumentation.packages.dbapi2 import (CursorProxy,
                                                    ConnectionProxy,
                                                    DbApi2Instrumentation,
                                                    extract_signature)


class MySQLCursorProxy(CursorProxy):
    provider_name = 'mysql'

    def _extract_signature(self, sql):
        return extract_signature(sql)

class MySQLConnectionProxy(ConnectionProxy):
    cursor_proxy = MySQLCursorProxy

class MySQLInstrumentation(DbApi2Instrumentation):
    name = 'mysql'

    instrument_list = [
        ("MySQLdb", "connect"),
    ]

    def call(self, module, method, wrapped, instance, args, kwargs):
        return MySQLConnectionProxy(wrapped(*args, **kwargs), self.client)
