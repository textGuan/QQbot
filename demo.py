# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import tkinter as tk
import shutil
import wx
import wx.xrc
import os
from tkinter import filedialog

import QQbot
import del_file

count = 1

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		if not (os.path.exists('temp')):
			os.mkdir('temp')
		if not (os.path.exists('workspace')):
			os.mkdir('workspace')
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = "COVID19-四川大学健康每日报-QQ群发助手", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )
		self.icon1=wx.Icon(name="favicon.ico",type=wx.BITMAP_TYPE_ICO)
		self.SetIcon(self.icon1)
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,  style = wx.TE_CENTER| wx.TE_MULTILINE|wx.TE_READONLY|wx.BORDER_NONE )
		bSizer13.Add( self.m_textCtrl3, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer13, 1, wx.EXPAND, 5 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, "\n\n\n不能提供检错功能因此若软件闪退，请检查文件格式是否正确\n\n\n望该工具早日被停止使用\n使用须知：必须先设置好名单、加载好截图\n完成以上步骤后设置消息，才能群发消息\n否则程序不能正常执行\n开发流程短未设置错误处理\n如果出错请关闭程序重新运行\n点击help菜单获取更多说明", wx.DefaultPosition, wx.DefaultSize, style = wx.TE_CENTER| wx.TE_MULTILINE )
		self.m_textCtrl1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer2.Add( self.m_textCtrl1, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer2, 15, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer4.Add( bSizer6, 1, wx.EXPAND, 5 )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.set_button = wx.Button( self, wx.ID_ANY, u"设置消息", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.set_button, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer12, 1, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.list_button = wx.Button( self, wx.ID_ANY, u"载入名单", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.list_button, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer7, 1, wx.EXPAND, 5 )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.sc_button = wx.Button( self, wx.ID_ANY, u"载入截图", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.sc_button, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer8, 1, wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.run_button = wx.Button( self, wx.ID_ANY, u"开始群发", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.run_button, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer9, 1, wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.exit_button = wx.Button( self, wx.ID_ANY, u"退出程序", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.exit_button, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer10, 1, wx.EXPAND, 5 )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer11.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer4.Add( bSizer11, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer4, 2, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, u"COVID-19 四川大学健康每日报适用", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_READONLY|wx.BORDER_NONE )
		self.m_textCtrl2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer5.Add( self.m_textCtrl2, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.file_menu_root = wx.Menu()
		self.start_menu = wx.MenuItem( self.file_menu_root, wx.ID_ANY, u"Start Sending", wx.EmptyString, wx.ITEM_NORMAL )
		self.file_menu_root.Append( self.start_menu )
		#edit
		self.start_menu.Enable(False)
		#edit

		self.set_menu = wx.MenuItem( self.file_menu_root, wx.ID_ANY, u"Set Message", wx.EmptyString, wx.ITEM_NORMAL )
		self.file_menu_root.Append( self.set_menu )

		self.list_menu = wx.MenuItem( self.file_menu_root, wx.ID_ANY, u"Load Students", wx.EmptyString, wx.ITEM_NORMAL )
		self.file_menu_root.Append( self.list_menu )

		self.sc_menu = wx.MenuItem( self.file_menu_root, wx.ID_ANY, u"Load Screenshots", wx.EmptyString, wx.ITEM_NORMAL )
		self.file_menu_root.Append( self.sc_menu )

		self.exit_menu = wx.MenuItem( self.file_menu_root, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.file_menu_root.Append( self.exit_menu )

		self.m_menubar1.Append( self.file_menu_root, u"File" )

		self.help_menu_root = wx.Menu()
		self.help_menu = wx.MenuItem( self.help_menu_root, wx.ID_ANY, u"Help", wx.EmptyString, wx.ITEM_NORMAL )
		self.help_menu_root.Append( self.help_menu )

		self.m_menubar1.Append( self.help_menu_root, u"Help" )

		self.about_root = wx.Menu()
		self.about_menu = wx.MenuItem( self.about_root, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.about_root.Append( self.about_menu )

		self.m_menubar1.Append( self.about_root, u"About" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.list_button.Bind( wx.EVT_BUTTON, self.list_buttonOnButtonClick )
		self.sc_button.Bind( wx.EVT_BUTTON, self.sc_buttonOnButtonClick )
		self.run_button.Bind( wx.EVT_BUTTON, self.run_buttonOnButtonClick )
		#edit
		self.run_button.Enable(False)
		#edit
		self.set_button.Bind( wx.EVT_BUTTON, self.set_buttonOnButtonClick )
		self.exit_button.Bind( wx.EVT_BUTTON, self.exit_buttonOnButtonClick )
		self.Bind( wx.EVT_MENU, self.start_menuOnMenuSelection, id = self.start_menu.GetId() )
		self.Bind( wx.EVT_MENU, self.set_menuOnMenuSelection, id = self.set_menu.GetId() )
		self.Bind( wx.EVT_MENU, self.list_menuOnMenuSelection, id = self.list_menu.GetId() )
		self.Bind( wx.EVT_MENU, self.sc_menuOnMenuSelection, id = self.sc_menu.GetId() )
		self.Bind( wx.EVT_MENU, self.exit_menuOnMenuSelection, id = self.exit_menu.GetId() )
		self.Bind( wx.EVT_MENU, self.help_menuOnMenuSelection, id = self.help_menu.GetId() )
		self.Bind( wx.EVT_MENU, self.about_menuOnMenuSelection, id = self.about_menu.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def list_buttonOnButtonClick( self, event ):
		#edit
		root = tk.Tk()
		root.withdraw()
		file_path = filedialog.askopenfilename()#get listfile path
		despath = '1.csv'
		# shutil.move(file_path,despath)
		shutil.copy2(file_path,despath)#copy
		self.start_menu.Enable(False)
		self.run_button.Enable(False)
		#edit
		# event.Skip()

	def sc_buttonOnButtonClick( self, event ):
		#edit
		del_file.sc()
		root = tk.Tk()
		root.withdraw()
		file_path = filedialog.askopenfilenames()
		num = len(file_path)
		count = 1
		for i in file_path:
			shutil.copy2(i,'workspace/'+str(count)+'.jpg')
			count = count+1
		self.start_menu.Enable(False)
		self.run_button.Enable(False)
		#edit
		# event.Skip()

	def run_buttonOnButtonClick( self, event ):
		#edit
		str1 = self.m_textCtrl1.GetValue()
		self.m_textCtrl3.Clear()
		if str1 == '':
			self.m_textCtrl3.SetValue("\n不能发送空消息")
		else:
			str_view = QQbot.run(str1)
			if str_view == "ERROR":
				self.m_textCtrl1.SetValue("可能是并发量达到限制或图片格式不对等\n请检查是否按照要求载入联系表数据库、截图等\n或稍后重试")
			elif str_view == "QQ_ERROR":
				self.m_textCtrl1.SetValue("请检查是否已经将qq界面置于最前")
			else:
				self.m_textCtrl1.SetValue("已经成功向以下qq账号\n"+str_view+"发送\n"+str1+"\n消息")
		self.start_menu.Enable(False)
		self.run_button.Enable(False)
		#edit
		# event.Skip()

	def exit_buttonOnButtonClick( self, event ):
		self.Close(True)
		# event.Skip()

	def set_buttonOnButtonClick( self, event ):
		#edit
		self.m_textCtrl1.Clear()
		self.m_textCtrl3.SetValue("请在下面输入您想群发的消息，完成后点击开始群发或File-Start Sending\n如果出现未响应提示等请稍安勿躁，通常需要几分钟时间处理，期间请不要进行任何操作")
		self.start_menu.Enable(True)
		self.run_button.Enable(True)
		#edit
		# event.Skip()

	def start_menuOnMenuSelection( self, event ):
		#edit
		str1 = self.m_textCtrl1.GetValue()
		self.m_textCtrl3.Clear()
		if str1 == '':
			self.m_textCtrl3.SetValue("\n不能发送空消息")
		else:
			self.m_textCtrl3.Clear()
			str_view = QQbot.run(str1)
			if str_view == "ERROR":
				self.m_textCtrl1.SetValue("可能是并发量达到限制或图片格式不对等\n请检查是否按照要求载入联系表数据库、截图等\n或稍后重试")
			elif str_view == "QQ_ERROR":
				self.m_textCtrl1.SetValue("请检查是否已经将qq界面置于最前")
			else:
				self.m_textCtrl1.SetValue("已经成功向以下qq账号\n"+str_view+"发送\n"+str1+"\n消息")
		self.start_menu.Enable(False)
		self.run_button.Enable(False)
		#edit
		# event.Skip()

	def set_menuOnMenuSelection( self, event ):
		#edit
		self.m_textCtrl1.Clear()
		self.m_textCtrl3.SetValue("请在下面输入您想群发的消息，完成后点击开始群发或File-Start Sending\n如果出现未响应提示等请稍安勿躁，通常需要几分钟时间处理，期间请不要进行任何操作")
		self.start_menu.Enable(True)
		self.run_button.Enable(True)
		#edit
		# event.Skip()

	def list_menuOnMenuSelection( self, event ):
		#edit
		root = tk.Tk()
		root.withdraw()
		file_path = filedialog.askopenfilename()
		despath = '1.csv'
		# shutil.move(file_path,despath)
		shutil.copy2(file_path,despath)
		self.start_menu.Enable(False)
		self.run_button.Enable(False)
		#edit
		# event.Skip()


	def sc_menuOnMenuSelection( self, event ):
		#edit
		global count
		del_file.sc()
		root = tk.Tk()
		root.withdraw()
		file_path = filedialog.askopenfilenames()
		num = len(file_path)
		for i in file_path:
			shutil.copy2(i,'workspace/'+str(count)+'.jpg')
			count = count+1
		self.start_menu.Enable(False)
		self.run_button.Enable(False)
		#edit
		# event.Skip()

	def exit_menuOnMenuSelection( self, event ):
		#edit
		self.Close(True)
		#edit
		# event.Skip()

	def help_menuOnMenuSelection( self, event ):
		help_text = "\n\n\n1.设置消息按钮或File-Set Message菜单：在当前文本控件输入需要群发的消息，支持使用“/”+字母的形式群发表情消息。\n"+"2.载入名单按钮或File-Load Students菜单：通过文件浏览器选择csv文件形式的学生与qq号对应的名单，csv文件内容每一行为 “学生姓名（中文全称）,QQ号码或QQ对应的邮箱账号”，例如:\n张三,123456789\n王二,stu987@qq.com\n"+"注意此处是英文逗号\n可以使用Microsoft Excel软件按行键入，编辑完成后另存为.csv格式即可。名单仅需载入一次，不必重复载入\n"+"3.载入截图按钮或File-Load Screenshots菜单：通过文件浏览器一次性选中所有截图（按住键盘ctrl键），截图要求如示例图片所示\n"+"4.开始群发按钮或File-Start Sending菜单：根据截图和名单找出所有未完成健康每日报的学生，并为其发送设置的消息\n"+"5.执行顺序必须为：先载入名单和截图（若无需更新则将使用本地名单和截图），再设置消息，才能开始群发，其他顺序将不能正常执行\n"
		self.m_textCtrl1.Clear()
		self.m_textCtrl1.SetValue(help_text)
		# event.Skip()

	def about_menuOnMenuSelection( self, event ):
		about_text = "\n\n\nAuthor: Norman Guan\n Date: 02/12/2020 \n E-mail:1157411076@qq.com \n QQ:1157411076@qq.com \n Github:github.com/textGuan \n WebPage: jyyj.fun"
		self.m_textCtrl1.Clear()
		self.m_textCtrl1.SetValue(about_text)
		# event.Skip()