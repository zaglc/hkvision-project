import typing
from PyQt5.QtCore import QObject
from controller import Controller
from viewer import Viewer
from PyQt5 import QtCore

import time
import numpy as np

class Camera():
    def __init__(self) -> None:
        self.viewer = Viewer()
        self.controller = Controller()
        
        pass


global_context = Camera()
