from transformers import MarianTokenizer, MarianMTModel

translator_model_name = "Helsinki-NLP/opus-mt-fr-en"
tokenizer = MarianTokenizer.from_pretrained(translator_model_name)
translator = MarianMTModel.from_pretrained(translator_model_name)

def translate_text(text, target_lang="en"):
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    translated = translator.generate(**inputs)
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    return translated_text