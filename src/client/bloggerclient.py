class BloggerClient:
    def __init__(self, config):
        self.__url = config.get("blogger", "url")
        self.__access_token = config.get("blogger", "access_token")

    def blog(self, pin_img):
        self.__attach_img(pin_img)

    def __attach_img(self, img):
        # ToDo: attach image to blog using blogger api