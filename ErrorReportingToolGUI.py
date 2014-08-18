#GUI for Error Reporting tool. Should pop up when an error log is scanned.

import sys
import wx
import webbrowser

class ErrorReporting(wx.Frame):
	def __init__(self, *args, **kw):
		super(ErrorReporting, self).__init__(*args, size=(500,500))
		self.ErrorReportingGUI()

	def ErrorReportingGUI(self) :
		ErrorReportingPanel = wx.Panel(self)
		hbox = wx.BoxSizer(wx.HORIZONTAL)
	
		KnownErrorsList = open('/Users/risanewyear-ramirez/Desktop/LogParserWorkTermProject/logparser//KnownErrors.txt', 'r')
		UnknownErrorsList = open('/Users/risanewyear-ramirez/Desktop/LogParserWorkTermProject/logparser//UnknownErrors.txt', 'r')
	
		# Set up the font, sizing, and boxes
		font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
		heading = wx.StaticText(self, label='Welcome to the Error Reporting Tool', pos=(140, 15))
		heading.SetFont(font)
		self.SetTitle( 'Error Reporting Tool')
		KnownErrorsTxtCtrl = wx.TextCtrl(ErrorReportingPanel, value=str(UnknownErrorsList), pos=(30, 90), size=(30,30), style=wx.TE_MULTILINE)
		UnknownErrorsListBox = wx.ListBox(ErrorReportingPanel, pos=(270, 90), size=(30,30), choices=str(KnownErrorsList), style=wx.LB_MULTIPLE)
		UnknownErrorsListBox.SetBackgroundColour(wx.Colour(0,0,0))
		self.Bind(wx.EVT_LISTBOX, self.OnUnknownErrorsListBox)
		
		hbox.Add(UnknownErrorsListBox, 1, wx.EXPAND | wx.ALL, 20)
		
	
		#Line for decoration and labels for boxes
		wx.StaticLine(self, pos=(25, 50), size=(300,1))
		KnownErrorsText = wx.StaticText(self, label='Known Errors', pos=(30, 80))
		KnownErrorsText.SetForegroundColour(wx.Colour(34,139,34))
		UnknownErrorsText = wx.StaticText(self, label='Unknown Errors', pos=(270, 80))
		UnknownErrorsText.SetForegroundColour(wx.Colour(255,0,0))
		wx.StaticLine(self, pos=(25, 260), size=(300,1))
	
		# When there are unknown errors present, report them to JIRA
		self.button =wx.Button(self, label="Report to JIRA", pos=(200, 325))
		self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)

		self.Centre()
		self.Show(True)

	def OnClick(self,event):
		webbrowser.open('https://sapjira.wdf.sap.corp/secure/ViewProfile.jspa/')
	def OnUnknownErrorsListBox(self, event):
		selection = self.UnknownErrorsListBox.GetSelection()

def main() :
	er = wx.App()
	ErrorReporting(None)
	er.MainLoop()

main()