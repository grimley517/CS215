import csv
G = {}
def makeLink(actor, film, G):
    if actor not in G:
        G[actor] = []
    if filem not in G:
        G[film] = []
    G[actor].append(film)
    G[film].append(actor)
    return G
with open('imdb-1.tsv','r') as tsvfile:
    dialect = csv.Sniffer().sniff(tsvfile.read(1024))
    tsvfile.seek(0)
    tsv = csv.reader(tsvfile, dialect)

try:
    for (actor, film, date) in tsv:
        film = film + ' ' + date
        makeLink(actor, film, G)
except UnicodeDecodeError as decodeError:
    print(decodeError)

print (G)
