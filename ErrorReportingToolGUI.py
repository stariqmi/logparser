#GUI for Error Reporting tool. Should pop up when an error log is scanned.

import sys
import wx
import wx.lib.agw.hyperlink as hl

class ErrorReporting(wx.Frame):
	def __init__(self, *args, **kw):
		super(ErrorReporting, self).__init__(*args, **kw)
		self.ErrorReportingGUI()

	def ErrorReportingGUI(self) :
		ErrorReportingPanel = wx.Panel(self)
	
		KnownErrorsList = open('KnownErrors.txt')
		UnknownErrorsList = open('UnknownErrors.txt')
	
		# Set up the font, sizing, and boxes
		font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
		heading = wx.StaticText(self, label='Welcome to the Error Reporting Tool', pos=(140, 15))
		heading.SetFont(font)
		self.SetTitle( 'Error Reporting Tool')
		self.UnknownErrorsTxtCtrl = wx.TextCtrl(ErrorReportingPanel, value=UnknownErrorsList, style=wx.TE_MULTILINE, size=(-1,295))
		self.KnownErrorsListBox = wx.ListBox(self, 26, wx.DefaultPosition, (170, 130), KnownErrorsList, wx.LB_SINGLE)
		
		#Link to JIRA
		JIRA = h1.HyperLinkCtrl(ErrorReportingPanel, -1, "JIRA", pos=(200,325), URL="https://sapjira.wdf.sap.corp/secure/ViewProfile.jspa/")
	
		#Line for decoration and labels for boxes
		wx.StaticLine(self, pos=(25, 50), size=(300,1))
		KnownErrorsText = wx.StaticText(self, label='Known Errors', pos=(30, 80))
		KnownErrorsText.SetForegroundColour((34,139,34))
		UnknownErrorsText = wx.StaticText(self, label='Unknown Errors', pos=(270, 80))
		UnknownErrorsText.SetForegroundColour(255,0,0))
		wx.StaticLine(self, pos=(25, 260), size=(300,1))
	
		# When there are unknown errors present, report them to JIRA
		self.button =wx.Button(self, label="Report to JIRA", pos=(200, 325))
		self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)

		self.Centre()
		self.Show(True)

	def OnClick(self,event):
		self.show(JIRA)


def main() :
	er = wx.App()
	ErrorReporting(None)
	er.MainLoop()

main()