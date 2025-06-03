from UserAgent import UserAgent
from TranslatorAgent import TranslatorAgent

def main():
    print("Welcome to Translator Agent 🤖")
    user_agent = UserAgent()
    translator_agent = TranslatorAgent()

    text = user_agent.get_input()
    target_lang = user_agent.get_target_language()
    
    translated_text = translator_agent.translate_text(text, target_lang)
    print(f"\nTranslated Text ({target_lang}): {translated_text}")

if __name__ == "__main__":
    main()
