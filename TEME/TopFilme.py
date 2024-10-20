utilizatori = [
    {
       'nume': 'George',
       'filme': ['Shrek', 'Bond', 'Fight Club']
    },
    {
       'nume': 'Cristian',
       'filme': ['Fight Club', 'The Nun', 'Dracula', 'Bond']
    },
    {
       'nume': 'Stefan',
       'filme': ['Fight Club', 'Slumdog Milionare']
    }
]
filme_count = {}

for utilizator in utilizatori:
    for film in utilizator['filme']:
        if film in filme_count:
            filme_count[film] += 1
        else:
            filme_count[film] = 1

cel_mai_vizionat_film = max(filme_count, key=filme_count.get)

print("Cel mai vizionat film:", cel_mai_vizionat_film)
cel_mai_vizionat_utilizator = utilizatori[0]

for utilizator in utilizatori:
    if len(utilizator['filme']) > len(cel_mai_vizionat_utilizator['filme']):
        cel_mai_vizionat_utilizator = utilizator

print("Utilizatorul cu cele mai multe filme vizionate:", cel_mai_vizionat_utilizator['nume'])

top_filme = sorted(filme_count.items(), key=lambda x: x[1], reverse=True)
print("Top filme dupa vizionari:", [film[0] for film in top_filme])

top_utilizatori = sorted(utilizatori, key=lambda u: len(u['filme']), reverse=True)
print("Top utilizatori cu cele mai multe filme vizionate:", [utilizator['nume'] for utilizator in top_utilizatori])
