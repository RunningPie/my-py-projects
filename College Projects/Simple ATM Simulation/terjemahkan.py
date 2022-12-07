from googletrans import Translator

def terjemahkan(teks, tujuan="id"):
    return Translator().translate(teks, tujuan).text