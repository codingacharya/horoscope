import streamlit as st
import datetime
import pdfkit
from io import BytesIO

def get_zodiac_sign(day, month):
    zodiac_signs = [
        ("Capricorn", (12, 22), (1, 19)),
        ("Aquarius", (1, 20), (2, 18)),
        ("Pisces", (2, 19), (3, 20)),
        ("Aries", (3, 21), (4, 19)),
        ("Taurus", (4, 20), (5, 20)),
        ("Gemini", (5, 21), (6, 20)),
        ("Cancer", (6, 21), (7, 22)),
        ("Leo", (7, 23), (8, 22)),
        ("Virgo", (8, 23), (9, 22)),
        ("Libra", (9, 23), (10, 22)),
        ("Scorpio", (10, 23), (11, 21)),
        ("Sagittarius", (11, 22), (12, 21)),
    ]
    for sign, start, end in zodiac_signs:
        if (month == start[0] and day >= start[1]) or (month == end[0] and day <= end[1]):
            return sign
    return "Unknown"

def generate_horoscope(zodiac_sign):
    horoscopes = {
        "Aries": "You will have a day full of energy and enthusiasm.",
        "Taurus": "A good day for making financial decisions.",
        "Gemini": "Your communication skills will shine today.",
        "Cancer": "Take care of your emotional well-being.",
        "Leo": "A great day to showcase leadership skills.",
        "Virgo": "Focus on organization and planning.",
        "Libra": "Balance is the key to your day.",
        "Scorpio": "A deep and meaningful conversation is coming your way.",
        "Sagittarius": "Adventure and excitement await you.",
        "Capricorn": "Hard work will pay off today.",
        "Aquarius": "Think outside the box and innovate.",
        "Pisces": "A creative breakthrough is on the horizon."
    }
    return horoscopes.get(zodiac_sign, "No horoscope available.")

def create_pdf(name, dob, zodiac_sign, horoscope):
    html = f"""
    <h1>Horoscope Details</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Date of Birth:</strong> {dob}</p>
    <p><strong>Zodiac Sign:</strong> {zodiac_sign}</p>
    <p><strong>Horoscope:</strong> {horoscope}</p>
    """
    pdf = pdfkit.from_string(html, False)
    return pdf

st.title("Horoscope Details Generator")
name = st.text_input("Enter your name:")
dob = st.date_input("Enter your Date of Birth:", min_value=datetime.date(1900, 1, 1))
if st.button("Generate Horoscope"):
    zodiac_sign = get_zodiac_sign(dob.day, dob.month)
    horoscope = generate_horoscope(zodiac_sign)
    st.write(f"**Name:** {name}")
    st.write(f"**Date of Birth:** {dob}")
    st.write(f"**Zodiac Sign:** {zodiac_sign}")
    st.write(f"**Horoscope:** {horoscope}")
    pdf_file = create_pdf(name, dob, zodiac_sign, horoscope)
    st.download_button(
        label="Download Horoscope as PDF",
        data=BytesIO(pdf_file),
        file_name=f"{name}_horoscope.pdf",
        mime="application/pdf"
    )
