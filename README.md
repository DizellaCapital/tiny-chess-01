# tiny-chess-01

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

It talks to the env at `MAKEFUN_ENV_URL` (`POST /game`, `POST /move`)
until the env answers `done`.
