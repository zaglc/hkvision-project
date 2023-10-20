import cv2

class Viewer():
    def __init__(self, login_config) -> None:
        
        assert (
            "NAME" in login_config and
            "PASSWD" in login_config and 
            "IP" in login_config and
            "PORT" in login_config and 
            "CHANNEL" in login_config
        ), "missing login info"

        name, passwd, ip, port, channel = (
            login_config["NAME"],
            login_config["PASSWD"],
            login_config["IP"],
            login_config["PORT"],
            login_config["CHANNEL"],           
        )

        self._url = f"{name}:{passwd}@{ip}/{port}/{channel}"
        self.cam = cv2.VideoCapture(self._url)
        
        pass
