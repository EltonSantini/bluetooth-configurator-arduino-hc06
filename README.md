# Bluetooth Configurator – Arduino + HC-06

Tooling to configure an **HC-06 Bluetooth module** using an **Arduino Nano Every** as a smart adapter.

The Arduino handles:
- Entering AT command mode
- Sending AT commands for **name / baud / PIN**
- Providing a simple **serial menu** over USB so a user can configure modules without knowing AT command syntax.

> This is a generic project and does not contain any employer-specific or proprietary code.

---

## ✨ Features

- Detects HC-06 module and attempts to enter **AT mode**
- Interactive serial menu:
  - View current settings
  - Change **device name**
  - Change **baud rate**
  - Change **PIN**
- Simple, well-commented Arduino code for learning AT command flows
- Optional **PC client** (Python) that wraps the serial menu in a nicer CLI

---

## 🧱 Suggested Project Layout

```text
bluetooth-configurator-arduino-hc06/
├─ src/
│  ├─ bluetooth_configurator.ino
│  └─ hc06_commands.h
├─ tools/
│  └─ pc_serial_client.py
├─ docs/
│  ├─ wiring-diagram.png
│  └─ protocol.md
└─ README.md
