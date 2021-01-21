import attr

from fastapi_utils.session import FastAPISessionMaker


@attr.s
class Session:
    reader_conn_string: str = attr.ib()
    writer_conn_string: str = attr.ib()

    def __attrs_post_init__(self):
        self.reader: FastAPISessionMaker = FastAPISessionMaker(self.reader_conn_string)
        self.writer: FastAPISessionMaker = FastAPISessionMaker(self.writer_conn_string)