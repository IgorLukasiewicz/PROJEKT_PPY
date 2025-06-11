Klasa Pet
=========

Opis
----

Klasa ``Pet`` reprezentuje wirtualne zwierzę, którym gracz może się opiekować.
Zawiera informacje o poziomie najedzenia i radości zwierzaka oraz pozwala na jego karmienie i zabawę.

Atrybuty
--------

- ``_name`` (str): Imię zwierzaka (domyślnie `None`, można ustawić później).
- ``satiety_points`` (int): Punkty najedzenia (0–100).
- ``_joy_points`` (int): Punkty radości (0–100).
- ``textureBeforeEvolve`` (str): Tekstura przed ewolucją.
- ``textureAfterEvolve`` (str): Tekstura po ewolucji.
- ``backgroundTexture`` (str): Tekstura tła.

Właściwości
-----------

- ``name``: Getter/setter imienia zwierzaka. Ustawia tylko niepuste ciągi tekstowe.
- ``joy_points``: Getter/setter punktów radości. Automatycznie ogranicza wartości do zakresu 0–100.

Metody
------

.. py:method:: play(additional_joy_points, taken_satiety_points)

   Zwiększa punkty radości i zmniejsza punkty najedzenia.

   :param additional_joy_points: Liczba punktów radości do dodania.
   :param taken_satiety_points: Liczba punktów najedzenia do odjęcia.

.. py:method:: feed(additional_satiety_points)

   Zwiększa punkty najedzenia. Maksymalna wartość to 100.

   :param additional_satiety_points: Liczba punktów najedzenia do dodania.

.. py:method:: __str__()

   Zwraca tekstową reprezentację obiektu: punkty radości i najedzenia.
