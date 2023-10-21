from PyQt5 import QtCore
import time
import numpy as np
from multiprocessing.connection import PipeConnection
from multiprocessing import Process
from multiprocessing.synchronize import Condition

class QThread4VideoDisplay(QtCore.QThread):

    send_signal = QtCore.pyqtSignal(np.ndarray, int)
    def __init__(
            self, 
            thread_id: int,
            cam_proc: Process,
            conn: PipeConnection,
            cond: Condition,
            parent: QtCore.QObject = None,
        ) -> None:

        super().__init__(parent)
        self.id = thread_id
        self.conn = conn
        self.cond = cond
    
    def run(self):
        # 发射后开始定时，并需求下一张，定时结束后再发射
        while True:
            self.cond.acquire(True)
            self.cond.notify_all()
            self.cond.release()

            try:
                frame = self.conn.recv()
            except EOFError:
                break
            
            self.send_signal.emit(frame, self.id)
            time.sleep(1/30)
