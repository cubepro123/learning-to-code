# chatbot.py
# This file contains the main chatbot logic for UniBot – the USIU Africa
# AI Student Assistant.
#
# It uses Google Gemini (gemini-1.5-flash) as the AI backend and injects
# USIU-specific knowledge so the assistant only answers USIU-related questions.

import os                           # Used to read environment variables
import google.generativeai as genai # Google Gemini AI library

# Import the USIU knowledge base string from our usiu_info module
from usiu_info import USIU_KNOWLEDGE_BASE


def run_chat():
    """
    Main function that starts the UniBot terminal chatbot.
    It greets the user, accepts input, calls Gemini, and prints responses.
    Type 'exit', 'quit', or 'bye' to end the session.
    """

    # ------------------------------------------------------------------ #
    # 1. Load the Gemini API key from the environment variable            #
    # ------------------------------------------------------------------ #
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        print(
            "\n[ERROR] GEMINI_API_KEY environment variable is not set.\n"
            "Please set it before running UniBot:\n"
            "  Linux/Mac : export GEMINI_API_KEY='your_key_here'\n"
            "  Windows   : set GEMINI_API_KEY=your_key_here\n"
            "Get a free key at: https://aistudio.google.com\n"
        )
        return  # Exit the function if there is no API key

    # Configure the Gemini library with our API key
    genai.configure(api_key=api_key)

    # ------------------------------------------------------------------ #
    # 2. Build the system prompt                                          #
    # ------------------------------------------------------------------ #
    # The system prompt tells Gemini who it is and provides the USIU
    # knowledge base as context.  This keeps the assistant focused on
    # USIU-related topics.
    system_prompt = f"""
You are UniBot, a friendly and helpful AI student assistant for USIU Africa
(United States International University – Africa).

Your job is to answer questions that new or prospective students might have
about USIU Africa — such as admissions, fees, courses, campus facilities,
student life, and contact information.

Use ONLY the information provided in the knowledge base below to answer
questions. If a student asks something that is not related to USIU Africa,
politely let them know that you can only help with USIU-related topics and
invite them to ask a USIU-related question.

Keep your answers clear, friendly, and easy to understand.

--- USIU AFRICA KNOWLEDGE BASE ---
{USIU_KNOWLEDGE_BASE}
--- END OF KNOWLEDGE BASE ---
"""

    # ------------------------------------------------------------------ #
    # 3. Initialise the Gemini model and start a chat session             #
    # ------------------------------------------------------------------ #
    try:
        # Create a GenerativeModel instance using the flash model
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=system_prompt,  # Inject the system context
        )

        # Start a new multi-turn chat session (keeps conversation history)
        chat = model.start_chat(history=[])

    except Exception as e:
        print(f"\n[ERROR] Could not initialise the Gemini model: {e}\n")
        return

    # ------------------------------------------------------------------ #
    # 4. Greet the user                                                   #
    # ------------------------------------------------------------------ #
    print("\n" + "=" * 60)
    print("  Welcome to UniBot – USIU Africa AI Student Assistant  ")
    print("=" * 60)
    print("Hi there! I'm UniBot 🎓")
    print("I'm here to answer your questions about USIU Africa.")
    print("Ask me about admissions, fees, courses, campus, and more!")
    print("(Type 'exit', 'quit', or 'bye' to end the chat)\n")

    # ------------------------------------------------------------------ #
    # 5. Main chat loop                                                   #
    # ------------------------------------------------------------------ #
    while True:
        # Get input from the user
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            # Handle Ctrl+C or piped input ending gracefully
            print("\n\nGoodbye! Good luck with your studies at USIU Africa! 👋")
            break

        # Skip empty input
        if not user_input:
            continue

        # Check if the user wants to exit
        if user_input.lower() in {"exit", "quit", "bye"}:
            print("\nUniBot: Goodbye! Best of luck at USIU Africa! 🎓👋\n")
            break

        # Send the user's message to Gemini and get a response
        try:
            response = chat.send_message(user_input)
            print(f"\nUniBot: {response.text}\n")

        except Exception as e:
            # Handle API errors gracefully without crashing
            print(
                f"\n[UniBot] Sorry, I ran into a problem while fetching "
                f"your answer. Please try again.\n(Technical detail: {e})\n"
            )
