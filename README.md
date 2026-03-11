# UniBot – USIU Africa AI Student Assistant

A Python-based AI chatbot that answers questions new students might have about
**USIU Africa (United States International University – Africa)**.  
UniBot runs entirely in the terminal and is powered by **Google Gemini**.

> 📚 Student project for **IST1020**

---

## What It Does

UniBot is a conversational assistant that can answer questions about:

- 📋 **Admissions** – entry requirements, how to apply, required documents, deadlines
- 💰 **Fees** – tuition costs, payment methods, scholarships, HELB loans
- 🏫 **Courses / Programmes** – available degrees across all schools
- 🏠 **Campus Facilities** – library, labs, sports, hostels, cafeteria, Wi-Fi, and more
- 🎉 **Student Life** – clubs, SGA, orientation, international community
- 📅 **Academic Calendar** – trimester dates and structure
- 📞 **Contact Information** – website, email, phone, and location

If you ask something unrelated to USIU Africa, UniBot will politely redirect you.

---

## Prerequisites

- **Python 3.8 or higher** installed on your machine
- A free **Google Gemini API key** — get one at [aistudio.google.com](https://aistudio.google.com)

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/cubepro123/learning-to-code.git
cd learning-to-code
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set your Gemini API key

**Linux / macOS:**
```bash
export GEMINI_API_KEY="your_key_here"
```

**Windows (Command Prompt):**
```cmd
set GEMINI_API_KEY=your_key_here
```

### 4. Run the chatbot

```bash
python usiu_assistant/main.py
```

---

## Example Conversation

```
============================================================
  Welcome to UniBot – USIU Africa AI Student Assistant  
============================================================
Hi there! I'm UniBot 🎓
I'm here to answer your questions about USIU Africa.
Ask me about admissions, fees, courses, campus, and more!
(Type 'exit', 'quit', or 'bye' to end the chat)

You: What are the admission requirements?

UniBot: To join USIU Africa as an undergraduate student, you need a minimum
grade of C+ (plus) in KCSE or an equivalent qualification. Accepted
equivalents include the International Baccalaureate (IB), GCE A-Levels,
and SAT scores.

You can apply online through the admissions portal at:
https://www.usiu.ac.ke/admissions

You'll need to submit:
- Certified copies of your academic transcripts / certificates
- National ID (Kenyan citizens) or a valid passport
- Two recent passport-size photographs
- A completed application form
- Payment confirmation for the application fee

Is there anything else you'd like to know? 😊

You: bye

UniBot: Goodbye! Best of luck at USIU Africa! 🎓👋
```

---

## Project Structure

```
learning-to-code/
├── usiu_assistant/
│   ├── __init__.py       ← Package marker
│   ├── usiu_info.py      ← USIU Africa knowledge base
│   ├── chatbot.py        ← Main chatbot logic (Gemini integration)
│   └── main.py           ← Entry point – run this file
├── requirements.txt      ← Python dependencies
└── README.md             ← This file
```

---

## Notes

- This project uses the `google-generativeai` Python package with the
  `gemini-1.5-flash` model.
- The chatbot's knowledge is limited to the information stored in
  `usiu_assistant/usiu_info.py`. Update that file to keep facts current.
- This is a **student project** created for **IST1020** at USIU Africa.
