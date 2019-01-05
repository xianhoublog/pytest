import wx


class MyFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(100, 50),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        gSizer2 = wx.GridSizer(0, 2, 0, 0)
        self.SetTitle(u'Cy')
        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"方法", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        gSizer2.Add(self.m_staticText1, 0, wx.ALL, 5)

        m_comboBox3Choices = ["Seturl"]
        self.m_comboBox3 = wx.ComboBox(self, wx.ID_ANY, m_comboBox3Choices[0], wx.DefaultPosition, wx.DefaultSize,
                                       m_comboBox3Choices, 0)
        gSizer2.Add(self.m_comboBox3, 0, wx.ALL, 5)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"参数", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        gSizer2.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.m_textCtrl13 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.m_textCtrl13, 0, wx.ALL, 5)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"参数", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        gSizer2.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.m_textCtrl14 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.m_textCtrl14, 0, wx.ALL, 5)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"参数", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        gSizer2.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.m_textCtrl15 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.m_textCtrl15, 0, wx.ALL, 5)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"参数", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        gSizer2.Add(self.m_staticText5, 0, wx.ALL, 5)

        self.m_textCtrl16 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.m_textCtrl16, 0, wx.ALL, 5)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"返回值", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        gSizer2.Add(self.m_staticText6, 0, wx.ALL, 5)

        self.m_textCtrl17 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.m_textCtrl17, 0, wx.ALL, 5)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"启动", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.m_button1, 0, wx.ALL, 5)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"执行", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.m_button4, 0, wx.ALL, 5)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"创建", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.m_button2, 0, wx.ALL, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"定制", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.m_button3, 0, wx.ALL, 5)

        self.m_textCtrl14.SetEditable(False)
        self.m_textCtrl15.SetEditable(False)
        self.m_textCtrl16.SetEditable(False)
        self.SetSizer(gSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


app = wx.App()
frame = MyFrame()
frame.Show()
app.MainLoop()
