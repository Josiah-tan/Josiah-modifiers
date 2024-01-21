# Josiah Modifiers

## Motivation

- Emily's one stroke modifiers are good (e.g. `TKPWFRPBLTZ` → `super(alt(control(shift(g))))`)
- However, in practice, we often have to two-stroke commands, cause of 'command prefixes' 😿
- Josiah modifiers aims to make these one strokable.
- e.g. vim
    - C-w + C-w (switch window)
    - escape + vim modifier command
- e.g. emacs
    - C-x + C-f (read file)
    - C-x + C-s (save file)
- e.g. tmux (terminal multiplexer)
    - prefix + literally any tmux command

## The Very Simple Solution

- Free up `EU` cluster and use Abby's left hand fingerspelling for i, e and u:

| Letter | Old Version | New Remapped |
|--------|-------------|--------------|
| e      | E           | SK           |
| i      | EU          | SKW          |
| u      | U           | WR           |

- e.g. (for emacs)
    - `TPFLTZ` → {#control(f)}{plover:clear_trans_state}
    - `#TPEFLTZ` → {#control(x) control(f)}{plover:clear_trans_state}
- (`clear_trans_state` clears translation state, good for text editing)

## Emacs Commands

- example layout for emacs (partially filled out)

| -  |        | Emily  | - | #   |        |              |
| E  | esc    | Escape | - | #E  | ctrl-x | Ex command   |
| U  | ctrl-b | tmUx   | - | #U  | ctrl-c | CUstomisable |
| EU |        |        | - | #EU |        |              |

## Vim Commands

plz learn through [plover-vim-tutor](https://github.com/Josiah-tan/plover-vim-tutor):

```
:help plover-vim-Josiah-modifiers

```
- example layout for neovim (partially filled out)

| -  |               | Emily  | - | #   | ctrl-j | control(j) |
| E  | esc           | Escape | - | #E  | ctrl-x | Ex command |
| U  | ctrl-b        | tmUx   | - | #U  |        |            |
| EU | ctrl-j ctrl-w | wIndow | - | #EU | ctrl-r | regIster   |

## Extended Layout (optional)

- pressing -LTZ sucks

| # | T | P | H | * | * | F | P | L | T | D |
| S | K | W | R | * | * | R | B | G | S | Z |
|   |   |   |   |   |   |   |   |   |   |   |
|   |   | A | O |   |   | E | U |   |   |   |

- Can use left/right hand asterisk instead

| # | T | P | H | @ | * | F | P | L | T | D |  
| S | K | W | R | @ | * | R | B | G | S | Z |  
|   |   |   |   |   |   |   |   |   |   |   |  
|   |   | A | O |   |   | E | U |   |   |   |  

- means you can use right hand Emily multipliers if you want:

- e.g.
- W@T → `{#w w w}{plover:clear_trans_state}`

| -G  | × 2 |
| -L  | × 3 |
| -LS | × 4 |

## Installation

- Download plover and find the executable
	- see this https://plover.readthedocs.io/en/latest/cli_reference.html for finding the location of plover depending on which platform you are using (Linux, Windows, etc.)
- Now run this command to install the library

``` bash
<plover_executable> -s plover_plugins install plover_vim plover-stenotype-vim
```

- add Josiah-modifiers-vim.py or Josiah-modifiers-emacs.py as a dictionary

## Installation (Optional)

- if you want to use left/right hand asterisk key (`@`)
    - in plover gui go select configure → system → plover-stenotype-vim

