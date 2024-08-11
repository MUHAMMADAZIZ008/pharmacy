import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QMessageBox
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl

class VideoBackground(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Video Background")
        self.setGeometry(100, 100, 800, 600) 

        self.video_widget = QVideoWidget()

        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.media_player.setVideoOutput(self.video_widget)


        video_url = QUrl.fromLocalFile("D:/dars python/RealProject/video/223459_small.mp4")  
        self.media_player.setMedia(QMediaContent(video_url))

        self.media_player.error.connect(self.handle_error)

        self.media_player.play()

        layout = QVBoxLayout()
        layout.addWidget(self.video_widget)
        self.setLayout(layout)

    def handle_error(self):
        error = self.media_player.errorString()
        QMessageBox.critical(self, "Media Player Error", f"Xato yuz berdi: {error}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoBackground()
    window.show()
    sys.exit(app.exec_())
