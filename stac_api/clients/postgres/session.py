import os

import attr

from fastapi_utils.session import FastAPISessionMaker


@attr.s
class Session:
    reader_conn_string: str = attr.ib()
    writer_conn_string: str = attr.ib()

    @classmethod
    def create_from_env(cls):
        return cls(
            reader_conn_string=os.environ["READER_CONN_STRING"],
            writer_conn_string=os.environ["WRITER_CONN_STRING"],
        )

    def __attrs_post_init__(self):
        self.reader: FastAPISessionMaker = FastAPISessionMaker(self.reader_conn_string)
        self.writer: FastAPISessionMaker = FastAPISessionMaker(self.writer_conn_string)
