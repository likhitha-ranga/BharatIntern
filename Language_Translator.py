from googletrans import Translator
def translate_text(text, target_lang):
    translator = Translator().translate(text, dest=target_lang)
    return translator.text

source_text = input("Enter the text ")
target_lang = input("Enter the destination language ")
translated_text = translate_text(source_text, target_lang)
print(f"Translated text: {translated_text}")
