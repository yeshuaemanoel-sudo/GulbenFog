import streamlit as st

def analyze_post(text):
    lower_text = text.lower()
    risk = "Low"
    behavior = "Theoretical"
    confidence = 0.4
    reason = "General discussion"

    if "refund" in lower_text and ("refuse" in lower_text or "no response" in lower_text):
        risk = "Exit Scam"
        behavior = "Vendor Alert"
        confidence = 0.86
        reason = "Mentions refund refusal and vendor behavior"

    elif "giveaway" in lower_text or "free btc" in lower_text:
        risk = "Honeypot"
        behavior = "Emotional Bait"
        confidence = 0.91
        reason = "Possible bait using free reward"

    return {
        "Risk": risk,
        "Behavior": behavior,
        "Confidence": confidence,
        "Reason": reason
    }

st.title("🧠 RedFlagGPT - تحلیل تهدید دارک‌نت")

st.markdown("Paste یک پست از دارک‌نت برای تحلیل:")

input_text = st.text_area("💬 متن پست", height=150)

if st.button("🚨 تحلیل کن"):
    if input_text:
        result = analyze_post(input_text)
        st.subheader("📊 خروجی تحلیل:")
        st.json(result)
    else:
        st.warning("لطفاً متنی وارد کنید.")
