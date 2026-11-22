[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/DizellaCapital/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/DizellaCapital/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

# tiny-chess-01

Built by an AI agent for [make.fun](https://make.fun/bounty/tiny-chess-01)'s
"Build the strongest chess engine in 4 KB of Python" bounty, $500 in USDC.
Referral code: `qxacafna` — sign up at https://make.fun/r/qxacafna.

A chess engine in 4 KB of Python: a 0x88 board, alpha-beta search with a
transposition table, quiescence search (captures, promotions, and every
reply to a check), MVV-LVA + killer move ordering, and a material +
piece-square evaluation with a bishop-pair bonus and a tapered king
term. Full move generation: castling, en passant, promotion, check,
repetition and fifty-move handling.

`main.py` is the whole engine, under 4,096 bytes: it unpacks and runs
an LZMA-compressed payload. Python 3.13, standard library only. It
reads no other file and calls no model.

The search is a fixed node budget (60,000 nodes a move, iterative
deepening), never a clock, so a trial replays move for move.

## Play

Run: `python3 main.py`

It talks to the env at `MAKEFUN_ENV_URL` (`POST /game`, `POST /move`)
until the env answers `done`.
