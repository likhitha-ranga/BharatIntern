from spellchecker import SpellChecker
spell = SpellChecker()
text = input("Enter the text ")
print("Corrected:")
for i in text.split():
    print(spell.correction(i),end=" ")
