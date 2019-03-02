
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from bs4 import BeautifulSoup
import threading 
from utillc import *
EKO()
class Render(QWebEngineView):
    def __init__(self, url):
        self.html = None
        self.app = QApplication(sys.argv)
        QWebEngineView.__init__(self)
        self.loadFinished.connect(self._loadFinished)
        #self.setHtml(html)
        EKO()
        self.load(QUrl(url))
        self.show()
        self.app.exec_()

    def _loadFinished(self, result):
        # This is an async call, you need to wait for this
        # to be called before closing the app
        EKO()
        
        self.page().toHtml(self._callable)

    def _callable(self, data):
        EKO()
        soup = BeautifulSoup(data, 'html.parser')
        value = soup.find('input', {'class': '_2erBM _20_tk '})
        EKOX(value)

        clss = "_2erBM _20_tk "
        ccc0 = "document.getElementsByClassName('" + clss + "')[0].click()"
        ccc = "document.getElementsByClassName('" + clss + "')[0].value = 'coucou'"
        ccc1 = "document.getElementsByClassName('_2sNbI _1xIyN GXQkc _2xk2l')[0].click()"
        ccc2 = "document.getElementsByClassName('tT3Ya')[0].click()"
        
        l = [ ccc0, ccc, ccc1 ]
        l = [ ccc0, ccc, ccc1, ccc2 ]
        self.i = 0        
        def done(v) :
            EKOX(v)
            self.i += 1
            if self.i < len(l) :
                self.page().runJavaScript(l[self.i], done)
        self.page().runJavaScript(l[self.i], done)                    

            
        #threading.Timer(5.0, gfg).start()
        
        self.html = data
        # Data has been stored, it's safe to quit the app
        #self.app.quit()

url = "https://www.google.fr/"
url="https://www.leboncoin.fr/caravaning/offres/"
render = Render(url).html

