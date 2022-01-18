from base import Base


class BBC(Base):
    url = 'https://www.bbc.com/'

    def __init__(self):
        super().__init__()

