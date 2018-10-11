Algorithm

1. kalla eftir dimensions (>=3)
    "Input dimension of the board:"
2. Prenta út borðið skv. dimension 
    When the game board is printed, each position is printed in a field of 5
    characters wide, right justified.
        {:>5}.format(dimension)
    2.1. Athuga hver staðan er í leiknum. Er annar hvor búinn að vinna?
    a. Ef nei - bjóða næsta leikmanni að gera
    b. Ef já - prenta út hver vann
        "Winner is: X/O"
    Hvenær er leikmaður búinn að vinna?
    a. þegar leikmaður hefur náð X eða O "n" oft í röð lárétt:
            1, 2n + 1, 3n + 1, osfrv.
    b. þegar leikmaður hefur náð X eða O "n" oft í röð lóðrétt:
            1, 1+n, (1+n)+n
    c. þegar leikmaður hefur náð X eða O "n" oft í röð á ská frá vinstri til hægri:
            1, 1n+2, 2n + 3, 3n + 4, 4n + 5 
    d. þegar leikmmaður hefur náð X eða O "n" oft í röð á ská frá hægri til vinstri:
            n, 2n + (n-1), 2n + (n-2), 3n + (n-3) 
3. Bjóða leikmanni X að gera.
4. Villuathugun: Villuskilaboð: "Illegal move!"
    a. input ekki tala - búa til function sem athugar hvort hægt er að breyta í tölu. 
    b. númer passar ekki við víddina ath. að vídddin er dimension (n). Þá er hægt að setja inn tölu
    sem er frá 1 uppí n*n - ef í range, passa að bæta við 1.
    c. X eða O hefur þegar notað reitinn. Þá þarf að lesa borðið eins og það var prentað út síðast og 
    athuga hvort talan sé enn þar (væntanlega hefur hún verið fjarlægð úr borðinu þegar leikmaður gerði)
    => í öll skipti, bjóða leikmanni aftur að gera þar til hann gerir legal move!
5. Breyta borðinu þannig að X sé nú á þeim reit sem hann tiltók.
6. Bjóða O að gera.
7. Endurtaka 2-6 þar til:
    a. Annar er búinn að vinna ( endar þá í 2.1. b)
    b. Búið er að spila alla reitina - prenta þá út "Draw!"