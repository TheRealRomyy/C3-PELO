
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from utils.functions import *
from gui import GUI

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

C3PELO = GUI(cast(interface, POINTER(IAudioEndpointVolume)))
C3PELO.buildGUI()