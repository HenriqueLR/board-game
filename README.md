Board Game, is a game simulation

### Requirements

    python3
    pip3

  recommended to create a virtual environment,
  to avoid library version problems

### Install

  you can install the project's dependencies,
  easily by running the command

    make install

### Run

    make run

  Output

    ######## RESULTS ########
    All timeouts: 48
    AVG rounds of a match: 218.64
    Percentage of wins behavior:
    -> impulsive: 26.67%
    -> demanding: 19.67%
    -> cautious: 25.33%
    -> random: 28.33%
    Behavior max win: random

### Tests

    make test

  Output

    7 passed in 0.03s
    Name                   Stmts   Miss  Cover   Missing
    ----------------------------------------------------
    __init__.py                0      0   100%
    board/__init__.py          0      0   100%
    board/default.py           9      2    78%   12-13
    player/__init__.py        31     19    39%   15, 18-22, 25-38
    player/npc.py             40     26    35%   9-14, 21-27, 34-39, 46-52
    tests/__init__.py          0      0   100%
    tests/test_board.py       12      0   100%
    tests/test_player.py      32      4    88%   30-33
    tests/test_utils.py        4      0   100%
    utils/__init__.py          0      0   100%
    utils/square.py            3      0   100%
    ----------------------------------------------------
    TOTAL                    131     51    61%

  this command generates a folder with html reports,
  in app/htmlcov

### Lint

  maybe you want to run lint guild style flake8,
  set verbosity to .flake8, guild style 100% complete,
  no errors pep :)

    make lint

### Fun

 you can read more about this challenge  folder

    docs/

 good fun
