import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QStackedWidget,
    QFileDialog,
    QListWidget
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from qr_generator import generate_qr
from history_manager import (
    save_history,
    get_history,
    clear_history
)
from qr_decoder import decode_qr
from qr_analyzer import detect_qr_type
from safety_checker import check_url_safety
from qr_templates import (
    create_wifi_qr,
    create_email_qr,
    create_phone_qr,
    create_whatsapp_qr,
    create_vcard_qr,
    create_calendar_qr
)

app = QApplication(sys.argv)

app.setStyleSheet("""
    QWidget {
        background-color: #202020;
        color: #ffffff;
        font-size: 14px;
    }

    QLineEdit {
        background-color: #2b2b2b;
        color: #ffffff;
        border: 1px solid #444444;
        border-radius: 4px;
        padding: 6px;
    }

    QPushButton {
        background-color: #333333;
        color: #ffffff;
        border: 1px solid #555555;
        border-radius: 4px;
        padding: 6px;
    }

    QPushButton:hover {
        background-color: #444444;
    }

    QPushButton:pressed {
        background-color: #555555;
    }

    QListWidget {
        background-color: #2b2b2b;
        color: #ffffff;
        border: 1px solid #444444;
    }
""")

# Main Window
window = QWidget()
window.setWindowTitle("Shr3sth's QR Toolkit")
window.resize(600, 700)
stack = QStackedWidget()


# Generate Page
generate_page = QWidget()
generate_layout = QVBoxLayout()
generate_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
generate_layout.setSpacing(15)

# History Page
history_page = QWidget()
history_layout = QVBoxLayout()

history_title = QLabel("History")
history_layout.addWidget(history_title)
clear_history_button = QPushButton("Clear History")
history_layout.addWidget(clear_history_button)
history_list = QListWidget()
history_layout.addWidget(history_list)

history_page.setLayout(history_layout)

# Templates Page
templates_page = QWidget()
templates_layout = QVBoxLayout()

templates_title = QLabel("Templates")

wifi_button = QPushButton("WiFi QR")
email_button = QPushButton("Email QR")
phone_button = QPushButton("Phone QR")
whatsapp_button = QPushButton("WhatsApp QR")
contact_button = QPushButton("Contact QR")
calendar_button = QPushButton("Calendar QR")

back_button_templates = QPushButton("← Back")

templates_layout.addWidget(templates_title)
templates_layout.addWidget(wifi_button)
templates_layout.addWidget(email_button)
templates_layout.addWidget(phone_button)
templates_layout.addWidget(whatsapp_button)
templates_layout.addWidget(contact_button)
templates_layout.addWidget(calendar_button)
templates_layout.addWidget(back_button_templates)

templates_page.setLayout(templates_layout)

# Inspector Page
inspector_page = QWidget()
inspector_layout = QVBoxLayout()

inspector_title = QLabel("Inspector")

upload_button = QPushButton("Upload QR")

decoded_label = QLabel("")
decoded_label.setWordWrap(True)
type_label = QLabel("")
type_label.setWordWrap(True)
safety_label = QLabel("")
safety_label.setWordWrap(True)

back_button_inspector = QPushButton("← Back")

inspector_layout.addWidget(inspector_title)
inspector_layout.addWidget(upload_button)
inspector_layout.addWidget(decoded_label)
inspector_layout.addWidget(type_label)
inspector_layout.addWidget(safety_label)
inspector_layout.addWidget(back_button_inspector)

inspector_page.setLayout(inspector_layout)

# WiFi Template Page
wifi_page = QWidget()
wifi_layout = QVBoxLayout()

wifi_title = QLabel("WiFi QR Generator")

ssid_input = QLineEdit()
ssid_input.setPlaceholderText("SSID")

password_input = QLineEdit()
password_input.setPlaceholderText("Password")

encryption_input = QLineEdit()
encryption_input.setPlaceholderText("Encryption (WPA/WEP)")

generate_wifi_button = QPushButton("Generate WiFi QR")

back_button_wifi = QPushButton("← Back")

wifi_layout.addWidget(wifi_title)
wifi_layout.addWidget(ssid_input)
wifi_layout.addWidget(password_input)
wifi_layout.addWidget(encryption_input)
wifi_layout.addWidget(generate_wifi_button)
wifi_layout.addWidget(back_button_wifi)

wifi_page.setLayout(wifi_layout)

# Email Template Page
email_page = QWidget()
email_layout = QVBoxLayout()

email_title = QLabel("Email QR Generator")

email_input = QLineEdit()
email_input.setPlaceholderText("Email Address")

subject_input = QLineEdit()
subject_input.setPlaceholderText("Subject")

body_input = QLineEdit()
body_input.setPlaceholderText("Body")

generate_email_button = QPushButton("Generate Email QR")
back_button_email = QPushButton("← Back")

email_layout.addWidget(email_title)
email_layout.addWidget(email_input)
email_layout.addWidget(subject_input)
email_layout.addWidget(body_input)
email_layout.addWidget(generate_email_button)
email_layout.addWidget(back_button_email)

email_page.setLayout(email_layout)

# Phone Template Page
phone_page = QWidget()
phone_layout = QVBoxLayout()

phone_title = QLabel("Phone QR Generator")

phone_input = QLineEdit()
phone_input.setPlaceholderText("Phone Number")

generate_phone_button = QPushButton("Generate Phone QR")

back_button_phone = QPushButton("← Back")

phone_layout.addWidget(phone_title)
phone_layout.addWidget(phone_input)
phone_layout.addWidget(generate_phone_button)
phone_layout.addWidget(back_button_phone)

phone_page.setLayout(phone_layout)


# WhatsApp Template Page
whatsapp_page = QWidget()
whatsapp_layout = QVBoxLayout()

whatsapp_title = QLabel("WhatsApp QR Generator")

whatsapp_number_input = QLineEdit()
whatsapp_number_input.setPlaceholderText("Phone Number")

whatsapp_message_input = QLineEdit()
whatsapp_message_input.setPlaceholderText("Message")

generate_whatsapp_button = QPushButton("Generate WhatsApp QR")

back_button_whatsapp = QPushButton("← Back")

whatsapp_layout.addWidget(whatsapp_title)
whatsapp_layout.addWidget(whatsapp_number_input)
whatsapp_layout.addWidget(whatsapp_message_input)
whatsapp_layout.addWidget(generate_whatsapp_button)
whatsapp_layout.addWidget(back_button_whatsapp)

whatsapp_page.setLayout(whatsapp_layout)


# Contact Template Page
contact_page = QWidget()
contact_layout = QVBoxLayout()

contact_title = QLabel("Contact QR Generator")

first_name_input = QLineEdit()
first_name_input.setPlaceholderText("First Name")

last_name_input = QLineEdit()
last_name_input.setPlaceholderText("Last Name")

contact_phone_input = QLineEdit()
contact_phone_input.setPlaceholderText("Phone Number")

contact_email_input = QLineEdit()
contact_email_input.setPlaceholderText("Email")

organization_input = QLineEdit()
organization_input.setPlaceholderText("Organization")

generate_contact_button = QPushButton("Generate Contact QR")

back_button_contact = QPushButton("← Back")

contact_layout.addWidget(contact_title)
contact_layout.addWidget(first_name_input)
contact_layout.addWidget(last_name_input)
contact_layout.addWidget(contact_phone_input)
contact_layout.addWidget(contact_email_input)
contact_layout.addWidget(organization_input)
contact_layout.addWidget(generate_contact_button)
contact_layout.addWidget(back_button_contact)

contact_page.setLayout(contact_layout)


# Calendar Template Page
calendar_page = QWidget()
calendar_layout = QVBoxLayout()

calendar_title = QLabel("Calendar QR Generator")

event_title_input = QLineEdit()
event_title_input.setPlaceholderText("Event Title")

start_time_input = QLineEdit()
start_time_input.setPlaceholderText("Start Time (YYYYMMDDTHHMMSS)")

end_time_input = QLineEdit()
end_time_input.setPlaceholderText("End Time (YYYYMMDDTHHMMSS)")

location_input = QLineEdit()
location_input.setPlaceholderText("Location")

description_input = QLineEdit()
description_input.setPlaceholderText("Description")

generate_calendar_button = QPushButton("Generate Calendar QR")

back_button_calendar = QPushButton("← Back")

calendar_layout.addWidget(calendar_title)
calendar_layout.addWidget(event_title_input)
calendar_layout.addWidget(start_time_input)
calendar_layout.addWidget(end_time_input)
calendar_layout.addWidget(location_input)
calendar_layout.addWidget(description_input)
calendar_layout.addWidget(generate_calendar_button)
calendar_layout.addWidget(back_button_calendar)

calendar_page.setLayout(calendar_layout)


# Title Label
label = QLabel("Welcome to QR Code Generator!")
generate_layout.addWidget(label)

# Text Input
text_input = QLineEdit()
text_input.setPlaceholderText(
    "Enter text, URL, or QR content..."
)
generate_layout.addWidget(text_input)

# Generate Button
generate_button = QPushButton("Generate QR")
generate_layout.addWidget(generate_button)

# Templates Button
templates_button = QPushButton("Templates")
generate_layout.addWidget(templates_button)

# History Button
history_button = QPushButton("History")
generate_layout.addWidget(history_button)

# Inspector Button
inspector_button = QPushButton("Inspector")
generate_layout.addWidget(inspector_button)

# Export Button
export_button = QPushButton("Export QR")
generate_layout.addWidget(export_button)

# Back Button
back_button = QPushButton("← Back")
history_layout.addWidget(back_button)

# Status Label
status_label = QLabel("")
generate_layout.addWidget(status_label)

# QR Image Display Area
qr_label = QLabel()
qr_label.setFixedSize(300, 300)
generate_layout.addWidget(qr_label)


def button_clicked():
    text = text_input.text()
    if not text.strip():
        status_label.setText("Please enter some text.")
        return

    generate_qr(text, "output/qr.png")
    save_history(text)

    pixmap = QPixmap("output/qr.png")
    pixmap = pixmap.scaled(300, 300)

    qr_label.setPixmap(pixmap)

    status_label.setText("QR generated successfully!")


def export_qr():
    file_path, _ = QFileDialog.getSaveFileName(
        window,
        "Save QR Code",
        "qr.png",
        "PNG Files (*.png)"
    )

    if not file_path:
        return

    pixmap = qr_label.pixmap()

    if pixmap:
        pixmap.save(file_path)

        status_label.setText(
            f"Saved to {file_path}"
        )


def clear_history_gui():
    clear_history()

    history_list.clear()

    status_label.setText(
        "History cleared."
    )


def show_history():
    history = get_history()

    history_list.clear()

    for item in reversed(history):
        history_list.addItem(
            f"{item['timestamp']} | {item['text']}"
        )

    stack.setCurrentWidget(history_page)


def show_generate():
    stack.setCurrentWidget(generate_page)


def show_inspector():
    stack.setCurrentWidget(inspector_page)


def upload_qr():
    file_path, _ = QFileDialog.getOpenFileName(
        window,
        "Select QR Image",
        "",
        "Images (*.png *.jpg *.jpeg)"
    )

    if not file_path:
        return

    result = decode_qr(file_path)

    if result:
        qr_type = detect_qr_type(result)

        if qr_type == "URL":
            safe = check_url_safety(result)

            if safe:
                safety_label.setText("Safety: Safe")
            else:
                safety_label.setText("Safety: Suspicious URL")
        else:
            safety_label.setText("")

        decoded_label.setText(
            f"Content:\n{result}"
        )

        type_label.setText(
            f"Type: {qr_type}"
        )

    else:
        decoded_label.setText("No QR code found.")
        type_label.setText("")
        safety_label.setText("")


def generate_template_qr(data):
    generate_qr(data, "output/qr.png")
    save_history(data)

    pixmap = QPixmap("output/qr.png")
    pixmap = pixmap.scaled(300, 300)

    qr_label.setPixmap(pixmap)

    status_label.setText("Template QR generated!")

    stack.setCurrentWidget(generate_page)


def show_templates():
    stack.setCurrentWidget(templates_page)


def show_wifi_page():
    stack.setCurrentWidget(wifi_page)


def show_email_page():
    stack.setCurrentWidget(email_page)


def show_phone_page():
    stack.setCurrentWidget(phone_page)


def show_whatsapp_page():
    stack.setCurrentWidget(whatsapp_page)


def show_contact_page():
    stack.setCurrentWidget(contact_page)


def show_calendar_page():
    stack.setCurrentWidget(calendar_page)


def generate_wifi_from_form():
    ssid = ssid_input.text()
    password = password_input.text()
    encryption = encryption_input.text()

    if not ssid:
        return

    if not encryption:
        encryption = "WPA"

    qr_data = create_wifi_qr(
        ssid,
        password,
        encryption
    )

    generate_template_qr(qr_data)


def generate_email_from_form():
    qr_data = create_email_qr(
        email_input.text(),
        subject_input.text(),
        body_input.text()
    )

    generate_template_qr(qr_data)


def generate_phone_from_form():
    qr_data = create_phone_qr(
        phone_input.text()
    )

    generate_template_qr(qr_data)


def generate_whatsapp_from_form():
    qr_data = create_whatsapp_qr(
        whatsapp_number_input.text(),
        whatsapp_message_input.text()
    )

    generate_template_qr(qr_data)


def generate_contact_from_form():
    qr_data = create_vcard_qr(
        first_name_input.text(),
        last_name_input.text(),
        contact_phone_input.text(),
        contact_email_input.text(),
        organization_input.text()
    )

    generate_template_qr(qr_data)


def generate_calendar_from_form():
    qr_data = create_calendar_qr(
        event_title_input.text(),
        start_time_input.text(),
        end_time_input.text(),
        location_input.text(),
        description_input.text()
    )

    generate_template_qr(qr_data)


generate_button.clicked.connect(button_clicked)

history_button.clicked.connect(show_history)

clear_history_button.clicked.connect(
    clear_history_gui
)

inspector_button.clicked.connect(show_inspector)

export_button.clicked.connect(export_qr)

back_button.clicked.connect(show_generate)

back_button_inspector.clicked.connect(show_generate)

templates_button.clicked.connect(show_templates)

back_button_templates.clicked.connect(show_generate)

upload_button.clicked.connect(upload_qr)

wifi_button.clicked.connect(show_wifi_page)

generate_wifi_button.clicked.connect(
    generate_wifi_from_form
)

back_button_wifi.clicked.connect(
    show_templates
)

email_button.clicked.connect(show_email_page)

phone_button.clicked.connect(show_phone_page)

whatsapp_button.clicked.connect(show_whatsapp_page)

contact_button.clicked.connect(show_contact_page)

calendar_button.clicked.connect(show_calendar_page)

generate_email_button.clicked.connect(
    generate_email_from_form
)

back_button_email.clicked.connect(
    show_templates
)

generate_phone_button.clicked.connect(
    generate_phone_from_form
)

back_button_phone.clicked.connect(
    show_templates
)

generate_whatsapp_button.clicked.connect(
    generate_whatsapp_from_form
)

back_button_whatsapp.clicked.connect(
    show_templates
)

generate_contact_button.clicked.connect(
    generate_contact_from_form
)

back_button_contact.clicked.connect(
    show_templates
)

generate_calendar_button.clicked.connect(
    generate_calendar_from_form
)

back_button_calendar.clicked.connect(
    show_templates
)

generate_page.setLayout(generate_layout)

stack.addWidget(generate_page)
stack.addWidget(history_page)
stack.addWidget(inspector_page)
stack.addWidget(templates_page)
stack.addWidget(wifi_page)
stack.addWidget(email_page)
stack.addWidget(phone_page)
stack.addWidget(whatsapp_page)
stack.addWidget(contact_page)
stack.addWidget(calendar_page)

stack.setCurrentWidget(generate_page)

main_layout = QVBoxLayout()
main_layout.addWidget(stack)

window.setLayout(main_layout)

window.show()

app.exec()
