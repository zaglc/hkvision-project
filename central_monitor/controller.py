from central_monitor.HCNetSDK import *

class Controller():
    def __init__(self) -> None:
        self.support_ctrl = [2,3,4]
        pass

    def handle_ctrl(self, op: int):
        assert op in self.support_ctrl
        pass