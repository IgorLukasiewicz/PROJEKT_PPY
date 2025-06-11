Klasa JoyGame
=============

Opis
----

Klasa ``JoyGame`` reprezentuje mini-grę, w której gracz porusza swoim zwierzęciem (Pet), aby łapać spadające ikony radości i tym samym zwiększać jego punkty radości.
Gra działa w oparciu o `pygame` i dynamicznie dopasowuje skalowanie oraz kolizje.

Atrybuty
--------

- ``background_surface``: Powierzchnia tła gry.
- ``pet_name`` (str): Nazwa zwierzaka (string odpowiadający nazwie pliku tekstury).
- ``pet_position_x`` (int): Pozycja x zwierzaka.
- ``pet_surface``: Obrazek zwierzaka po skalowaniu.
- ``pet_rect``: Prostokąt kolizyjny zwierzaka.
- ``pet_speed`` (int): Prędkość poruszania się zwierzaka.
- ``falling_blocks`` (list): Lista obiektów klasy ``FallingBlock``.
- ``number_of_blocks`` (int): Liczba bloków na szerokość ekranu.

Metody
------

.. py:method:: __init__(pet, screen_width, screen_height, scale=1)

   Inicjalizuje grę, wczytuje tekstury i ustawia pozycje elementów.

.. py:method:: resize(surface, scale)

   Skaluje wszystkie elementy gry w zależności od rozmiaru okna.

.. py:method:: change_pet(pet_name)

   Zmienia teksturę aktualnego zwierzaka.

.. py:method:: draw(surface, scale)

   Rysuje tło, zwierzaka i aktywne bloki na podanej powierzchni.

.. py:method:: activate_falling_blocks(frame_counter)

   Co kilka klatek aktywuje losowy blok do spadania (jeśli jest nieaktywny).

.. py:method:: move_pet_left(surface)

   Przesuwa zwierzaka w lewo. Przejście poza ekran ustawia go po prawej stronie.

.. py:method:: move_pet_right(surface)

   Przesuwa zwierzaka w prawo. Przejście poza ekran ustawia go po lewej stronie.

.. py:method:: collision()

   Sprawdza kolizję zwierzaka z blokiem. Jeśli kolizja nastąpiła, ustawia blok jako trafiony i zwraca ``True``.


Klasa FallingBlock
===================

Opis
----

Klasa ``FallingBlock`` reprezentuje pojedynczy obiekt (ikonę radości), który spada z góry ekranu.
Może zostać aktywowany, rysowany i skalowany. Bloki mogą zostać złapane przez zwierzaka lub spaść poza ekran.

Atrybuty
--------

- ``position_x, position_y`` (int): Aktualna pozycja bloku.
- ``block_surface``: Powierzchnia z teksturą bloku.
- ``block_rect``: Prostokąt kolizyjny bloku.
- ``falling_speed`` (int): Prędkość spadania.
- ``hit`` (bool): Czy blok został złapany przez zwierzaka.
- ``set_for_fall`` (bool): Czy blok został aktywowany i ma spadać.

Metody
------

.. py:method:: __init__(starting_position_x, starting_position_y, scale=1)

   Tworzy nowy blok w pozycji startowej.

.. py:method:: resize(scale, surface, base_surface_width=1280, base_surface_height=720)

   Skaluje blok i dostosowuje jego pozycję względem aktualnego rozmiaru ekranu.

.. py:method:: draw(surface, scale=1)

   Rysuje blok na podanej powierzchni. Przesuwa go w dół o określoną prędkość.
