Klasa Pingwin
==============

Opis
----

Klasa ``Pingwin`` dziedziczy po klasie ``Pet`` i reprezentuje konkretne zwierzę – pingwina.
Ustawia domyślne tekstury oraz tło odpowiadające jego naturalnemu środowisku.

Atrybuty
--------

Dziedziczone po klasie ``Pet``:

- ``satiety_points`` (int): Punkty najedzenia (0–100).
- ``joy_points`` (int): Punkty radości (0–100).
- ``name`` (str): Imię zwierzaka.
- ``textureBeforeEvolve`` (str): Ścieżka do tekstury przed ewolucją.
- ``textureAfterEvolve`` (str): Ścieżka do tekstury po ewolucji.
- ``backgroundTexture`` (str): Ścieżka do tekstury tła.

W konstruktorze klasy ``Kameleon`` wartości są inicjalizowane jak poniżej:

- ``textureBeforeEvolve``: `"Assets/Images/PetsTxt/BeforeEvolution/pingwin.png"`
- ``textureAfterEvolve``: `""`
- ``backgroundTexture``: `"Assets/Images/Backgrounds/AnimalBackgrounds/Antarktyda.png"`

Metody
------

Dziedziczone z klasy ``Pet``:

- ``play(additional_joy_points, taken_satiety_points)``
- ``feed(additional_satiety_points)``

