#  [start:stop:step]

puno_ime = "Djordje Momcilov"
ime = puno_ime[0:7]
prezime = puno_ime[8:] #ne mora da se stavlja indeks uvek ako oces da ide od 
#pocetak do kraj Python automatski predpostavlja da se krece od 0 ili ide do kraj
#samo mora da stavis :
svako_drugo = puno_ime[::2]
okrenuto_ime = puno_ime[::-1]
print(ime, prezime, svako_drugo, okrenuto_ime)

# slicing
web_site1 = "http://google.com"
web_site2 = "http://wikipedia.com"
sl = slice(7,-4)
print(web_site1[sl])

