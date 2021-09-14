# 18. ABASTRACT BASE CLASSES - its purpose is to provide some common code to these derivitives
from abc import ABC, abstractmethod

class InvalidOperationError(Exception):
  pass

class Stream(ABC): #1  # 2. define the common interfaces for all streams 
  def __init__(self):
    self.opened = False

  def open(self):
    if self.opened:
      raise IndentationError("Stream is already open.")
    self.opened = True

  def close(self):
    if not self.opened:
      raise IndentationError("Stream is already closed.")
    self.opened = False

  @abstractmethod
  def read(self):
    pass
class FileStream(Stream):
  def read(self):
    print("Reading data from a file")

class NetworkStream(Stream):
  def read(self):
    print("Reading data from a network")

class MemoryStream(Stream):
  def read(self):
    print("Readiing data from a memory stream.")

#stream = Stream()
stream = MemoryStream()
stream.open()