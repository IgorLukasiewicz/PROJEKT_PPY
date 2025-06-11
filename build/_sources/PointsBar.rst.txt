Klasa PointsBar
===============

Opis
----

Klasa ``PointsBar`` odpowiada za graficzne przedstawienie paska punktów głodu i radości pupila w grze.
Umożliwia renderowanie paska z ikoną, tłem i dynamiczną liczbą zielonych segmentów odpowiadających aktualnym punktom.

Atrybuty klasowe
----------------

- ``green_bar_texture``: Wspólna tekstura zielonego paska dla wszystkich instancji.
- ``red_bar_texture``: Wspólna tekstura czerwonego tła paska dla wszystkich instancji.

Atrybuty instancji
------------------

- ``name`` (str): Nazwa paska (np. „Hunger”, „Joy”).
- ``points`` (int): Liczba punktów (od 0 do 100).
- ``rect`` (tuple): Pozycja i rozmiar prostokąta, gdzie pasek ma być rysowany.
- ``scale`` (int): Skala rysowania paska.
- ``bar_icon``: Ikona wyświetlana obok paska (np. buźka, żarcie).
- ``red_bar_surface``: Powierzchnia czerwonego tła paska.
- ``green_bar_surface``: Lista powierzchni dla segmentów zielonych (start, środek, koniec).

Metody
------

.. py:method:: __init__(name, points, bar_icon_path, rect, scale=1)

   Inicjalizuje obiekt ``PointsBar``.

   :param name: Nazwa paska (str).
   :param points: Początkowa liczba punktów (int).
   :param bar_icon_path: Ścieżka do pliku z ikoną paska (str).
   :param rect: Prostokąt do rysowania paska (x, y, width, height).
   :param scale: Skala rysowania (domyślnie 1).

.. py:method:: draw(surface)

   Rysuje pasek na podanej powierzchni Pygame.

   :param surface: Powierzchnia `pygame.Surface`, na której pasek ma być narysowany.

Działanie metody `draw`
-----------------------

Metoda:

- Rysuje ikonę paska.
- Następnie rysuje czerwone tło paska.
- W zależności od wartości `points`, rysuje odpowiednią liczbę zielonych segmentów:
  - Segment początkowy, środkowe i końcowy (start, middle, end) są ładowane z tekstury-spritesheet.
  - Każdy segment odpowiada za ~5 punktów.
