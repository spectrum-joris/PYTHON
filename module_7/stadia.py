# ASCII Art met raw strings (r"""...""") voor speciale tekens, zodat escape-tekens niet nodig zijn. "\" bijvoorbeeld wordt niet geïnterpreteerd."

HANGMAN_STAGES = [
r"""  +---+
  |   |
      |
      |
      |
      |
========""",
r"""  +---+
  |   |
  O   |
      |
      |
      |
========""",
r"""  +---+
  |   |
  O   |
  |   |
      |
      |
========""",
r"""  +---+
  |   |
  O   |
 /|   |
      |
      |
========""",
r"""  +---+
  |   |
  O   |
 /|\  |
      |
      |
========""",
r"""  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========""",
r"""  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========"""
]
