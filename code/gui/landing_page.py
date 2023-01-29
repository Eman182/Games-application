from params import *
from backend_layer.facade import Facade

class LandingWindow(QWidget):

    def init_progressbar(self):
        progressbar = QProgressBar(self)
        progressbar.setGeometry(land_page_progressbar_size)
        progressbar.setFont(font_landing)
        progressbar.setStyleSheet("QProgressBar\n")
        progressbar.setProperty("value", 24)
        progressbar.setStyleSheet(progressbar_landing_sheet)
        return progressbar

    def init_quote_lb(self):
        f = Facade.get_instance()
        lb = QLabel(self)
        lb.setGeometry(QtCore.QRect(160, 900, 400, 80))
        # TODO get random quote
        #lb.setText("this the quot this this the quot this the quot this the quot")
        lb.setText(f.get_quote()[0])
        lb.setStyleSheet(quote_sheet)
        lb.setWordWrap(True)
        #lb.setScaledContents(True)
        lb.setAlignment(QtCore.Qt.AlignCenter)
        lb.setFont(font_landing)
        return lb

    def __init__(self, parent=None):
        super(LandingWindow, self).__init__(parent)
        # resize window
        self.resize(QSize(landing_width, landing_height))
        # loading progressbar
        self.progressBar = self.init_progressbar()
        # quote label
        self.quote = self.init_quote_lb()


class LandingMain(QMainWindow):
    def __init__(self, parent=None):
        super(LandingMain, self).__init__(parent)
        # position of window
        self.setGeometry(600, 35, 600, 750)
        # size of window
        self.setFixedSize(landing_width, landing_height)
        self.startUIWindow()
        # background
        self.movie = QMovie(landing_bcg)
        self.movie.frameChanged.connect(self.repaint)
        self.movie.start()

    def startUIWindow(self):
        self.Window = LandingWindow(self)
        self.setWindowTitle(landing_title)
        self.show()

    def paintEvent(self, event):
        currentFrame = self.movie.currentPixmap()
        frameRect = currentFrame.rect()
        frameRect.moveCenter(self.rect().center())
        if frameRect.intersects(event.rect()):
            painter = QPainter(self)
            painter.drawPixmap(frameRect.left(), frameRect.top(), currentFrame)
