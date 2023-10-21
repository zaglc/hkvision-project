from PyQt5 import QtCore
import time
import numpy as np

from central_monitor.camera_top import global_context as gpc

class QThread4VideoDisplay(QtCore.QThread):

    def __init__(self, parent: QtCore.QObject) -> None:
        super().__init__(parent)
        self.send_signal = QtCore.pyqtSignal(np.ndarray)
    
    def run(self):
        while True:
            frame = gpc.viewer.fetch_frame()
            self.send_signal.emit(frame)
            time.sleep(1/10)
