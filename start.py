import wx
import demo

class CalcFrame(demo.MyFrame1): 
   def __init__(self,parent): 
      demo.MyFrame1.__init__(self,parent)  
 
def main():        
    app = wx.App(False) 
    frame = CalcFrame(None) 
    frame.Show(True) 
    #start the applications 
    app.MainLoop() 
 
if __name__ == '__main__':
    main()
