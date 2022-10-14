import google.cloud.texttospeech as tts
import pdfplumber


def chose_language():
    lang = input("Is the source text EN or FR? ").upper()
    if lang == "FR":
        return "fr-CA-Wavenet-B"
    elif lang == "EN":
        return "en-UK-Wavenet-B"
    else:
        print("Language not supported.")
        chose_language()


def pdf_to_text():
    file = input("Which pdf file do you want to use? ")
    with pdfplumber.open(file) as pdf:
        content = pdf.pages[0]
        extracted_text = content.extract_text()
        return extracted_text


def text_to_wav(voice_name: str, text: str):
    language_code = "-".join(voice_name.split("-")[:2])
    text_input = tts.SynthesisInput(text=text)
    voice_params = tts.VoiceSelectionParams(
        language_code=language_code, name=voice_name
    )
    audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.LINEAR16)

    client = tts.TextToSpeechClient()
    response = client.synthesize_speech(
        input=text_input, voice=voice_params, audio_config=audio_config
    )

    filename = f"{language_code}.wav"
    with open(filename, "wb") as out:
        out.write(response.audio_content)
        print(f'Generated speech saved to "{filename}"')


print("\n" + " Text to speech converter ".center(40, "-") + "\n")

text_to_wav(chose_language(), pdf_to_text())
