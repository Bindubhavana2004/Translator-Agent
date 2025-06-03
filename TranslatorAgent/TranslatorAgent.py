from translate import Translator

class TranslatorAgent:
    def translate_text(self, text, target_lang):
        try:
            translator = Translator(to_lang=target_lang)
            return translator.translate(text)
        except Exception as e:
            return f"Error: {str(e)}"
