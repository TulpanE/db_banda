import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLabel, QLineEdit
from server.db.DB_manager import DBmanager
base_manager = DBmanager("D:/PythonProjects/src/server/banda.db")


class View(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(650, 300)
        layout = QVBoxLayout()
        view_button = QPushButton('View Database fakewebsites')
        view_button.clicked.connect(self.view_database)

        self.view_messages = QPushButton('View Database Messages')
        self.view_messages.clicked.connect(self.view_message)

        self.view_records = QPushButton('add record')
        self.view_records.clicked.connect(self.add_record)

        self.table_widget = QTableWidget()
        layout.addWidget(view_button)
        layout.addWidget(self.view_messages)
        layout.addWidget(self.view_records)
        layout.addWidget(self.table_widget)
        self.setLayout(layout)

    def view_database(self):
        self.table_widget.setColumnCount(6)
        res = base_manager.execute("SELECT * FROM fakewebsites")

        self.table_widget.setRowCount(len(res))

        for row, (websiteid, url, purpose, victimcount, outcome, operationid) in enumerate(res):
            websiteid_item = QTableWidgetItem(str(websiteid))
            url_item = QTableWidgetItem(url)
            purpose_item = QTableWidgetItem(str(purpose))
            victimcount_item = QTableWidgetItem(str(victimcount))
            outcome_item = QTableWidgetItem(str(outcome))
            operationid_item = QTableWidgetItem(str(operationid))

            self.table_widget.setItem(row, 0, websiteid_item)
            self.table_widget.setItem(row, 1, url_item)
            self.table_widget.setItem(row, 2, purpose_item)
            self.table_widget.setItem(row, 3, victimcount_item)
            self.table_widget.setItem(row, 4, outcome_item)
            self.table_widget.setItem(row, 5, operationid_item)

    def view_message(self):
        self.table_widget.setColumnCount(4)
        res = base_manager.execute("SELECT * FROM messages")

        self.table_widget.setRowCount(len(res))

        for row, (messageid, content, status, operationid) in enumerate(res):
            messageid_item = QTableWidgetItem(str(messageid))
            content_item = QTableWidgetItem(content)
            status_item = QTableWidgetItem(str(status))
            operationid_item = QTableWidgetItem(str(operationid))

            self.table_widget.setItem(row, 0, messageid_item)
            self.table_widget.setItem(row, 1, content_item)
            self.table_widget.setItem(row, 2, status_item)
            self.table_widget.setItem(row, 3, operationid_item)

    def add_record(self):
        dialog = AddRecordDialog()
        dialog.exec_()


class AddRecordDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Add Record')
        layout = QVBoxLayout()
        self.url_label = QLabel('URL:')
        self.url_input = QLineEdit()
        self.purpose_label = QLabel('Purpose:')
        self.purpose_input = QLineEdit()
        self.victim_count_label = QLabel('Victim Count:')
        self.victim_count_input = QLineEdit()
        self.outcome_label = QLabel('Outcome:')
        self.outcome_input = QLineEdit()
        self.operation_id_label = QLabel('Operation ID:')
        self.operation_id_input = QLineEdit()
        self.add_button = QPushButton('Add Record')
        self.add_button.clicked.connect(self.add_record)
        layout.addWidget(self.url_label)
        layout.addWidget(self.url_input)
        layout.addWidget(self.purpose_label)
        layout.addWidget(self.purpose_input)
        layout.addWidget(self.victim_count_label)
        layout.addWidget(self.victim_count_input)
        layout.addWidget(self.outcome_label)
        layout.addWidget(self.outcome_input)
        layout.addWidget(self.operation_id_label)
        layout.addWidget(self.operation_id_input)
        layout.addWidget(self.add_button)
        self.setLayout(layout)

    def add_record(self):
        url = self.url_input.text()
        purpose = self.purpose_input.text()
        victim_count = int(self.victim_count_input.text())
        outcome = self.outcome_input.text()
        operation_id = int(self.operation_id_input.text())

        base_manager.execute("INSERT INTO fakewebsites (url, purpose, victimcount, outcome, operationid) VALUES (?, ?, ?, ?, ?)", (url, purpose, victim_count, outcome, operation_id))
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view_db_form = View()
    view_db_form.show()
    sys.exit(app.exec_())
