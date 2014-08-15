#gui for Error Reporting tool. Should pop up when an error log is scanned.


import wx

ErrorReportingTool = wx.App(False)
GUI = wx.Frame(None, wx.ID_ANY, "Welcome to the Error Reporting Tool")
GUI.Show(True)
ErrorReportingTool.MainLoop()