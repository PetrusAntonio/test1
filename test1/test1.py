def load_words_from_file(file_path):
    """Citește cuvintele dintr-un fișier și returnează două liste: una pentru cuvinte complete și alta pentru cuvinte incomplete."""
    complete_words = []
    incomplete_words = []
    
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split(';')  # Separă cuvintele pe baza spațiului
            complete_words.append(words[2])
            incomplete_words.append(words[1])
            
    
    return complete_words, incomplete_words


def find_matching_complete_words(incomplete_words, complete_words):
    """Compară cuvintele incomplete cu cele complete pentru a găsi potriviri și numără încercările, limitând la 1200."""
    matches = []
    total_attempts = 0  # Contor pentru încercări

    for incomplete in incomplete_words:
        for complete in complete_words:
            if len(complete)==len(incomplete):
                total_attempts += 1  # Incrementăm contorul pentru fiecare comparație
                if total_attempts > 1200:  # Verificăm dacă am depășit limita
                    print("Numărul maxim de încercări a fost atins (1200).")
                    return matches, total_attempts
                if complete.startswith(incomplete):  # Verifică dacă cuvântul complet începe cu cuvântul incomplet
                    matches.append(complete)
                    break  # Odată găsită o potrivire, se poate ieși din buclă

    return matches, total_attempts


# Exemplu de utilizare
file_path = 'cuvinte_de_verificat.txt'  # Numele fișierului care conține cuvintele
complete_words, incomplete_words = load_words_from_file(file_path)
matched_words, total_attempts = find_matching_complete_words(incomplete_words, complete_words)

# Afișează rezultatul
print("Cuvinte complete care se potrivesc cu cele incomplete:")
for word in matched_words:
    print(word)

# Afișează numărul total de încercări
print(f"Numărul total de încercări: {total_attempts}")
