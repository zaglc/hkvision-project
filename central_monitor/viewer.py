import cv2
import numpy as np

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

        self._url = f"rtsp://{name}:{passwd}@{ip}/Streaming/Channels/{channel}"
        self.cam = cv2.VideoCapture(self._url)
        
    def fetch_frame(self, need_frame = True) -> np.ndarray | None:
        if need_frame:
            ret, frame = self.cam.read()
        else:
            ret, frame = self.cam.grab(), None

        if not ret:
            raise RuntimeError(
                "frame fetch error"
            )
        return frame
    
    def reset_cam(self):
        self.cam.release()
        
