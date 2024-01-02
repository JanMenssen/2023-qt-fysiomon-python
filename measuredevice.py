#
# measuredevice.py
#
#     abstract class for the devices used. This class should be used as superclass for the specific
#     devices
#
#   modifications
#     15-dec-2023   JM    initial version

from PySide6.QtCore import QSettings

class measureDevice() :

  # constructor

  def __init__(self) :
    self.m_started = False
    return
  
  # initialise
  #
  #   initialises this dummy device, nothing is done

  def initialise(self) :
    return
  
  # isStarted
  #
  #   this function returns the started state

  def isStarted(self) :
    return self.m_started
  
  # setStartStop
  #
  #   this function sets the start/stop state of the device

  def setStartStop(self,mode) :
    self.m_started = mode
    return
  
  # iniRead
  #
  #   read the standard values 
  #     - analog in
  #     - numeric in
  #     - waveform in 

  def iniRead(self,name) :
    
    print("--> In measureDevice.iniRead")
     
    settings = QSettings(QSettings.IniFormat,QSettings.UserScope,"JanSoft",name)

    settings.beginGroup("algemeen")
    settings.endGroup()

    return