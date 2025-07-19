import streamlit as st
from whatsapp import format_number, send_whatsapp_message

# --- Rishta Profiles ---
male_profiles = [
    {"name": "Hassan Khn", "age": 28, "city": "Lahore", "profession": "Software Engineer"},
    {"name": "Bilal ", "age": 39, "city": "Karachi", "profession": "Doctor"},
    {"name": "Usman Ali", "age": 26, "city": "Islamabad", "profession": "Businessman"},
     {"name": "Fahad ", "age": 22, "city": "Islamabad", "profession": "Developer"}
    
]

female_profiles = [
    {"name": "Alizah", "age": 18, "city": "Karachi", "profession": "Full-Stack Developer"},
    {"name": "Hina Sheikh", "age": 27, "city": "Lahore", "profession": "Teacher"},
    {"name": "Minaal Zahra", "age": 25, "city": "Rawalpindi", "profession": "Graphic Designer"}
]

# --- Page Setup ---
st.set_page_config(page_title="Rishta Matchmaker 👰🤵", page_icon="💖")

# --- Modern Style ---
st.markdown("""
<style>
body {
    background-color: #000000;
    color: #ffffff;
}
.stApp {
    background-color: #000000;
    font-family: 'Segoe UI', sans-serif;
    padding: 10px;
}
h1 {
    color: #ff69b4;
    text-align: center;
    font-size: 48px;
    margin-bottom: 10px;
}
h3 {
    text-align: center;
    color: #cccccc;
    font-weight: normal;
    margin-bottom: 40px;
}
.stButton>button {
    background-color: #ff69b4;
    color: white;
    font-size: 16px;
    border-radius: 8px;
    padding: 10px 20px;
    box-shadow: 0 4px 12px rgba(255, 105, 180, 0.4);
    border: none;
}
.stTextInput>div>input, .stNumberInput input, .stSelectbox div, .stTextArea textarea {
    background-color: #111;
    color: #fff;
    border-radius: 6px;
    border: 1px solid #555;
}
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("<h1>💍 Rishta Matchmaker</h1>", unsafe_allow_html=True)
st.markdown("<h3>Find your perfect match — powered by GenAI, styled by Alizah 💖</h3>", unsafe_allow_html=True)

# --- Form ---
with st.form("rishta_form"):
    st.markdown("### 👤 Your Information")
    name = st.text_input("Full Name")
    age = st.slider("Your Age", 18, 100, 25)
    gender = st.selectbox("Gender", ["Male", "Female"])
    city = st.text_input("Your City")
    profession = st.text_input("Your Profession")
    recipient_number = st.text_input("WhatsApp Number")
    submitted = st.form_submit_button("📨 Send Rishta")

# --- Match Logic ---
def find_closest_match(user_age, profiles):
    return min(profiles, key=lambda x: abs(x['age'] - user_age))

if submitted:
    if not all([name.strip(), city.strip(), profession.strip(), recipient_number.strip()]):
        st.error("❌ Please fill all fields before sending.")
    else:
        formatted_number = format_number(recipient_number)
        if not formatted_number:
            st.error("❌ Invalid WhatsApp number.")
        else:
            profiles = female_profiles if gender == "Male" else male_profiles
            match = find_closest_match(age, profiles)

            message = f"""💍 *Rishta Proposal Alert!* 💍

Hello *{name}*! A new match has been found for you through *Rishta Matchmaker Bot* 🤖

🔹 *Name:* {match['name']}  
🔹 *Age:* {match['age']}  
🔹 *City:* {match['city']}  
🔹 *Profession:* {match['profession']}  
🔹 *Marital Status:* Single

If you're interested, reply back and we’ll discuss further. ❤  
Let’s help you find your perfect match!

_This proposal was sent via Rishta Matchmaker Bot 🤖_
"""

            result = send_whatsapp_message(formatted_number, message)
            if result.get("sent"):
                st.success(f"✅ Rishta sent to {match['name']} on WhatsApp!")
            else:
                st.error("❌ WhatsApp message failed to send.")

# --- Footer ---
st.markdown("""
<hr>
<div style="text-align:center; font-size:14px; color:#888; padding-top: 15px;">
Made with ❤️ by <b style="color:#e91e63;">Alizah</b> — Your GenAI Rishta Expert 💌
</div>
""", unsafe_allow_html=True)
