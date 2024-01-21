from contextlib import suppress

# import the modules that you want for your vim experience here
from plover_vim.Josiah_modifier.builtins import Lookup as JosiahModifierLookup


LONGEST_KEY = 1


Josiah_modifier_lookup = JosiahModifierLookup({
    "disable_defaults": False,
    # any dictionary entry overiddes the defaults
    "spelling": {},  # dict: right hand finger spelling
    "symbols": {},  # dict: left hand symbols
    "shifted": {},  # set: any symbols that should be shifted
    "unique_ender": "-LTZ", # Emily ender
    # "unique_ender": "@", # Josiah ender (requires plover-stenotype-vim)
    "prefixes": {
        "#": "",
        "E": "escape",  # 
        "EU": "",  # 
        "#EU": "",  # 
        "U": "control(b)",  # tmUx
        "#E": "control(x)",  # Ex command
        "#U": "control(c)",  # CUstomisable
        "": "",
        },
    # "numbers": { # (requires plover-stenotype-vim)
    #     "-S": "2",
    #     "-T": "3",
    #     "-TS": "4",
    #     }
    })


assert Josiah_modifier_lookup.dictionary.longest_key == LONGEST_KEY


def lookup(key):
    for look in [Josiah_modifier_lookup]:
        with suppress(KeyError):
            return look(key)


if __name__ == "__main__":
    Josiah_modifier_lookup.generateJson() # (optional convert to json format)

