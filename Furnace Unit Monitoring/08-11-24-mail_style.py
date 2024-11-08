import smtplib

SERVER = "mail.taropumps.com"
FROM = "RPI@taropumps.com"
TO = ["suresh.palanisamy@taropumps.com"]

SUBJECT = "TEXMO INDUSTRIES FURNACE UPT"

# Example data values
DATA1 = "123"
DATA2 = "1234"
DATA3 = "123545"

# Data entries for the table
data_entries = [
    {"label": "Data 1", "value": DATA1, "color": "blue"},
    {"label": "Data 2", "value": DATA2, "color": "green"},
    {"label": "Total Data", "value": DATA3, "color": "purple"},
]

# HTML message with a header, message, and a table
table_rows = "".join([
    f"""
    <tr>
        <td style="color: red; font-size: 10px;">{entry['label']}:</td>
        <td style="color: {entry['color']}; font-size: 10px;">{entry['value']}</td>
    </tr>
    """ for entry in data_entries
])

message = f"""\
From: {FROM}
To: {", ".join(TO)}
Subject: {SUBJECT}
MIME-Version: 1.0
Content-Type: text/html; charset="utf-8"

<html>
  <body style="font-family: 'Times New Roman', Times, serif; font-size: 12px;">
    <h2 style="font-weight: bold;">Furnace Energy Consumption Data:</h2>
    <p>Furnace Energy Consumption Data: <strong style="color: red;">{DATA3}</strong></p>
    
    <table border="1" style="border-collapse: collapse; width: 100%;">
      <tr>
        <th style="color: red; font-size: 12px;">Description</th>
        <th style="color: red; font-size: 12px;">Value</th>
      </tr>
      {table_rows}
    </table>
  </body>
</html>
"""

# Sending the email
try:
    with smtplib.SMTP(SERVER) as server:
        server.sendmail(FROM, TO, message)
    print("Email sent successfully.")
except Exception as e:
    print(f"Failed to send email: {e}")