from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QComboBox,
    QStackedWidget,
)

from PySide6.QtGui import QShortcut, QKeySequence, QPixmap
from PySide6.QtCore import Qt

from trainer import Trainer

from PySide6.QtWidgets import (
    QMainWindow,
    QComboBox,
    QPushButton,
    QVBoxLayout,
    QWidget
)

from Vocabulary import (
    Vocabulary_Nicos_Weg_A2_0,
    Vocabulary_Nicos_Weg_A2_1,
    Vocabulary_Nicos_Weg_A2_2,
    Vocabulary_Nicos_Weg_A2_3
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("German Vocabulary Trainer")
        self.resize(500, 300)

        # ==================================================
        # VOCABULARIES
        # ==================================================

        self.vocabularies = {
            "Nico's Weg A2 Chapter 0": Vocabulary_Nicos_Weg_A2_0,
            "Nico's Weg A2 Chapter 1": Vocabulary_Nicos_Weg_A2_1,
            "Nico's Weg A2 Chapter 2": Vocabulary_Nicos_Weg_A2_2,
            "Nico's Weg A2 Chapter 3": Vocabulary_Nicos_Weg_A2_3,
        }

        self.trainer = None
        self.current_word = None

        # ==================================================
        # MODE MENU
        # ==================================================

        self.mode_menu = QComboBox()

        self.mode_menu.addItems([
            "Consecutive",
            "Random",
            "Image Game"
        ])

        self.mode_menu.model().item(2).setEnabled(False)

        self.current_mode = None

        # ==================================================
        # STACKED WIDGET
        # ==================================================

        self.pages = QStackedWidget()

        self.setCentralWidget(self.pages)

        # ==================================================
        # SELECTION PAGE
        # ==================================================

        self.selection_page = QWidget()

        selection_layout = QVBoxLayout()

        self.vocabulary_menu = QComboBox()
        self.vocabulary_menu.addItems(self.vocabularies.keys())

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_trainer)

        vocabulary_label = QLabel("Vocabulary")

        selection_layout.addWidget(vocabulary_label)
        selection_layout.addWidget(self.vocabulary_menu)

        mode_label = QLabel("Mode")

        selection_layout.addWidget(mode_label)
        selection_layout.addWidget(self.mode_menu)

        selection_layout.addWidget(self.start_button)

        self.selection_page.setLayout(selection_layout)

        self.pages.addWidget(self.selection_page)

        # ==================================================
        # TRAINER PAGE
        # ==================================================

        self.trainer_page = QWidget()

        trainer_layout = QVBoxLayout()

        # ---------- Word ----------

        self.wordLabel = QLabel()
        self.wordLabel.setAlignment(Qt.AlignCenter)
        self.wordLabel.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
            padding: 15px;
        """)

        trainer_layout.addWidget(self.wordLabel)

        # ---------- Image ----------

        self.imageLabel = QLabel()
        self.imageLabel.setFixedSize(400, 250)
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.imageLabel.setStyleSheet("""
            border: 1px solid #555;
            background-color: #2d2d2d;
        """)

        imageLayout = QHBoxLayout()
        imageLayout.addStretch()
        imageLayout.addWidget(self.imageLabel)
        imageLayout.addStretch()

        trainer_layout.addLayout(imageLayout)

        # ---------- Answer ----------

        self.answerBox = QLineEdit()
        self.answerBox.setPlaceholderText("Type the translation")

        trainer_layout.addWidget(self.answerBox)

        # ---------- Buttons ----------

        self.checkButton = QPushButton("Check")

        self.showAnswerButton = QPushButton("Show Answer")
        self.showAnswerButton.setEnabled(False)

        buttonLayout = QHBoxLayout()

        buttonLayout.addWidget(self.checkButton)
        buttonLayout.addWidget(self.showAnswerButton)

        trainer_layout.addLayout(buttonLayout)

        # ---------- Result ----------

        self.resultLabel = QLabel()
        self.resultLabel.setAlignment(Qt.AlignCenter)

        trainer_layout.addWidget(self.resultLabel)

        # ---------- Next ----------

        self.nextButton = QPushButton("Next")
        self.nextButton.setEnabled(False)

        trainer_layout.addWidget(self.nextButton)

        self.trainer_page.setLayout(trainer_layout)

        self.pages.addWidget(self.trainer_page)

        # Start on selection page
        self.pages.setCurrentWidget(self.selection_page)

        # ==================================================
        # STYLE
        # ==================================================

        self.setStyleSheet("""
        QMainWindow {
            background-color: #1e1e1e;
        }

        QWidget {
            background-color: #1e1e1e;
            color: white;
        }

        QLabel {
            color: white;
            font-size: 18px;
        }

        QLineEdit {
            background-color: #2d2d2d;
            color: white;
            border: 1px solid #555;
            border-radius: 5px;
            padding: 8px;
            font-size: 18px;
        }

        QComboBox {
            background-color: #2d2d2d;
            color: white;
            border: 1px solid #555;
            border-radius: 5px;
            padding: 8px;
            font-size: 18px;
        }

        QPushButton {
            background-color: #3c3c3c;
            color: white;
            border-radius: 5px;
            padding: 8px;
            font-size: 16px;
        }

        QPushButton:hover {
            background-color: #505050;
        }

        QPushButton:disabled {
            background-color: #222;
            color: #666;
        }
        """)

        # ==================================================
        # CONNECTIONS
        # ==================================================

        self.checkButton.clicked.connect(self.check_answer)
        self.showAnswerButton.clicked.connect(self.show_answer)
        self.nextButton.clicked.connect(self.next_question)

        self.answerBox.returnPressed.connect(self.check_answer)

        QShortcut(
            QKeySequence("Ctrl+Return"),
            self,
            activated=self.show_answer
        )

        QShortcut(
            QKeySequence("Ctrl+Enter"),
            self,
            activated=self.show_answer
        )

        QShortcut(
            QKeySequence("Ctrl+Shift+N"),
            self,
            activated=self.next_question
        )

    def start_trainer(self):

        selected_name = self.vocabulary_menu.currentText()

        vocabulary = self.vocabularies[selected_name]

        self.current_mode = self.mode_menu.currentText()

        self.trainer = Trainer(vocabulary)

        self.pages.setCurrentWidget(self.trainer_page)

        if self.current_mode == "Consecutive":
            self.next_word()

        elif self.current_mode == "Random":
            self.random_word()

    def display_word(self, word):

        self.current_word = word

        self.wordLabel.setText(word.question)

        if word.image:

            from pathlib import Path

            image_path = Path(__file__).parent / word.image
            pixmap = QPixmap(str(image_path))

            if not pixmap.isNull():

                self.imageLabel.setPixmap(
                    pixmap.scaled(
                        self.imageLabel.size(),
                        Qt.KeepAspectRatio,
                        Qt.SmoothTransformation,
                    )
                )

                self.imageLabel.show()

            else:

                self.imageLabel.clear()
                self.imageLabel.hide()

        else:

            self.imageLabel.clear()
            self.imageLabel.hide()

        self.answerBox.clear()
        self.answerBox.setFocus()

        self.resultLabel.clear()

        self.showAnswerButton.setEnabled(False)
        self.nextButton.setEnabled(False)

    def next_word(self):

        word = self.trainer.next_word()

        if word is None:
            self.end_name()
            return

        self.display_word(word)

    def random_word(self):

        word = self.trainer.random_word()

        self.display_word(word)
    
    def check_answer(self):

        answer = self.answerBox.text().strip()

        if answer.lower() == self.current_word.answer.lower():

            self.current_word.correct += 1

            self.resultLabel.setText("✔ Correct!")

            self.nextButton.setEnabled(True)

        else:

            self.current_word.wrong += 1

            self.resultLabel.setText("✘ Wrong! Try again.")

            self.showAnswerButton.setEnabled(True)

            self.answerBox.clear()
            self.answerBox.setFocus()

    def show_answer(self):

        self.resultLabel.setText(
            f"Answer: {self.current_word.answer}"
        )

        self.nextButton.setEnabled(True)

    def next_question(self):

        if self.current_mode == "Consecutive":
            self.next_word()

        elif self.current_mode == "Random":
            self.random_word()

    def end_game(self):

        self.wordLabel.setText("Vocabulary complete!")
        self.imageLabel.clear()
        self.imageLabel.hide()

        self.answerBox.clear()
        self.answerBox.setEnabled(False)

        self.checkButton.setEnabled(False)
        self.showAnswerButton.setEnabled(False)
        self.nextButton.setEnabled(False)    