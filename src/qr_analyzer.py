def detect_qr_type(data):
    if data.startswith("http://") or data.startswith("https://"):
        return "URL"

    if data.startswith("WIFI:"):
        return "WiFi"

    if data.startswith("mailto:"):
        return "Email"

    if data.startswith("tel:"):
        return "Phone"

    if data.startswith("BEGIN:VCARD"):
        return "Contact Card"

    if "wa.me" in data:
        return "WhatsApp"

    if data.startswith("BEGIN:VEVENT"):
        return "Calendar Event"

    return "Plain Text"
