from spell_checker import SpellChecker

def main():
    spell_checker = SpellChecker("wortliste.txt")

    print("🔍 IntelliSpell – Deutscher Spell Checker")
    text = input("Gib deinen deutschen Text ein:\n> ")

    results = spell_checker.check_text(text)

    print("\n📋 Ergebnisse:")
    for item in results:
        if not item['correct']:
            print(f"❌ '{item['word']}' ist falsch. Vorschläge: {item['suggestions']}")
        else:
            print(f"✅ '{item['word']}' ist korrekt.")

if __name__ == "__main__":
    main()
