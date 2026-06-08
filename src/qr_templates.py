def create_wifi_qr(ssid, password, encryption="WPA"):
    return (
        f"WIFI:T:{encryption};"
        f"S:{ssid};"
        f"P:{password};;"
    )


def create_email_qr(email, subject="", body=""):
    return (
        f"mailto:{email}"
        f"?subject={subject}"
        f"&body={body}"
    )


def create_phone_qr(phone_number):
    return f"tel:{phone_number}"


def create_whatsapp_qr(phone_number, message=""):
    return (
        f"https://wa.me/{phone_number}"
        f"?text={message}"
    )


def create_vcard_qr(
    first_name,
    last_name,
    phone="",
    email="",
    organization=""
):
    return (
        "BEGIN:VCARD\n"
        "VERSION:3.0\n"
        f"N:{last_name};{first_name}\n"
        f"FN:{first_name} {last_name}\n"
        f"ORG:{organization}\n"
        f"TEL:{phone}\n"
        f"EMAIL:{email}\n"
        "END:VCARD"
    )


def create_calendar_qr(
    title,
    start_time,
    end_time,
    location="",
    description=""
):
    return (
        "BEGIN:VEVENT\n"
        f"SUMMARY:{title}\n"
        f"DTSTART:{start_time}\n"
        f"DTEND:{end_time}\n"
        f"LOCATION:{location}\n"
        f"DESCRIPTION:{description}\n"
        "END:VEVENT"
    )
