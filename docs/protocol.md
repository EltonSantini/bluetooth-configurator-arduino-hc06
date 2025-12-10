# HC-06 Configuration Protocol (Notes)

This document outlines how the Arduino sketch interacts with the HC-06 module
using simple AT commands.

## AT Mode

Many HC-06 modules enter AT mode when:

- The module is powered with a specific key pin held (varies by board), or
- The baud rate is set to 9600 and the module is not paired.

This project assumes the module is already in a state where AT commands are accepted.

## Commands Used

- `AT` – test command, should respond with `OK`
- `AT+NAME?` – query current name (varies by firmware)
- `AT+NAME<newname>` – set new name
- `AT+PIN<pin>` – set new PIN

Always check your exact module's documentation: HC-06 clones may behave slightly differently.
