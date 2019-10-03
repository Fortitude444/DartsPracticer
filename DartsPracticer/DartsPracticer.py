import wpf
#using IronPython;
#using IronMath;

from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'DartsPracticer.xaml')
    

if __name__ == '__main__':
    Application().Run(MyWindow())
