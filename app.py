import streamlit as st import openai import os

1. הגדרת מפתחות API (שים את המפתח שלך פה או השתמש ב-secrets)

openai.api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else os.getenv("OPENAI_API_KEY")

2. כותרת ראשית באפליקציה

st.title("🛒 השוואת מחירים חכמה עם AI") st.write("הזן מוצר שאתה מחפש, ואנחנו נבין מה חשוב לך ונחזיר תוצאות בהמשך.")

3. קלט מהמשתמש

user_input = st.text_input("מה אתה מחפש?")

4. כפתור לשליחה

if st.button("🔍 חפש") and user_input: with st.spinner("GPT מנתח את הבקשה שלך..."): prompt = f""" אתה עוזר קניות חכם. המשתמש כתב: "{user_input}" תספק את הנתונים הבאים בפורמט JSON: - "product": שם המוצר - "max_price": מחיר מקסימלי אם מופיע - "preferences": רשימת העדפות (למשל משלוח מהיר, דירוג גבוה) - "language": האם החיפוש בעברית או באנגלית """

try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4
        )
        st.success("הבקשה פוענחה בהצלחה!")
        st.json(response.choices[0].message.content)
    except Exception as e:
        st.error(f"שגיאה בקריאה ל-GPT: {e}")

5. תזכורת למפתח

st.caption("הערה: יש להוסיף את מפתח OpenAI ב-secrets או כמשתנה סביבה בשם OPENAI_API_KEY")
