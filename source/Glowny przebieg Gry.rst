===================
Echo Pets - Przebieg Gry
===================

Opis:
    Główna pętla gry oparta na Pygame. Obsługuje stany gry: menu główne, tworzenie nowej gry (wybór pupila i wpisanie nazwy),
    rozgrywkę (z jedzeniem i zabawą) oraz kontrolę dźwięku.


Najważniejsze zmienne globalne:
    - `fps`: klatki na sekundę (60)
    - `BASE_WIDTH`, `BASE_HEIGHT`: bazowe wymiary okna
    - `width`, `height`: aktualne wymiary okna (początkowo takie jak bazowe)
    - `gameState`: aktualny stan gry („menu”, „nowa gra”, „makePet”, „playing”, „feeding”, „joy_game”)
    - `pet`, `pet_Type`: obiekt pupila i typ
    - `textField`, `textFieldText`: do wpisywania nazwy pupila oraz przechowywania jego imienia
    - `button_list`: lista aktywnych przycisków potrzebnych dla danego stanu gry

Ładowanie stanu gry:
    Czytanie pliku `lastGame.txt`, wypełnianie `lines`, wybór typu pupila i stworzenie obiektu z odpowiednimi statystykami:
    radość i sytość. W przypadku pustego pliku jest on wypelniony pustymi znakami ""

Glowne funkcje :
    - `shouldButtonMakeASound()`: obsługuje kliknięcia przycisków i sprawdza czy powinien on wydac przypisany do siebie dźwięk
    - `closeGame()`: kończy grę
    - `changeGamestateToMenu()`: powrót do menu — zapisuje stan, przełącza muzykę
    - `baw_sie()`: inicjuje tryb zabawowy (`joy_game`)
    - `nakarm()`: inicjuje feedowanie – pojawia się tło, losowo jedzenie, obsługa kliknięć na jedzenie
    - `runGame()`: główny sposób przejścia do rozgrywki — ładowanie grafiki, przycisków, muzyki
    - `setup_menu_buttons()`, `setup_new_game_buttons()`: generowanie przycisków w różnych stanach
    - `poWyborze(text)`: po wyborze pupila – wpisanie nazwy

Obsługa zdarzeń:
    - `QUIT`: zamknięcie gry
    - `VIDEORESIZE`: dostosowanie układu do nowego rozmiaru
    - Obsługa klawiatury (strzałki w `joy_game`)
    - Obsługa myszki w `feeding` (kliknięcie w jedzenie)

Pętla główna:
    - W zależności od `gameState` wywołuje odpowiednie rysowanie i logikę:
        - **menu**: tło animowane, przyciski
        - **nowa gra**: tło wyboru, przyciski
        - **makePet**: wpisywanie nicku (TextField)
        - **playing**: rysowanie paska sytości i radości, przyciski
        - **feeding**: wyświetlanie tła, losowe pojawianie jedzenia, kliknięcia feedujące pupila
        - **joy_game**: logika minigry z poruszaniem pupila i kolizjami

Wysyłanie kliknięciowy dźwięków przyciskom oraz odtwarzanie efektów podczas karmienia lub zdobywania punktów radości.
