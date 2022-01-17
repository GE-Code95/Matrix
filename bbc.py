from base import Base

url = 'https://www.bbc.com/'


class BBC(Base):
    def __init__(self, driver):
        super().__init__(driver)
