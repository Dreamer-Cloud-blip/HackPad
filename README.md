# SixPad

A compact, custom-designed screwless 6-key mechanical macropad built with a Seeeduino XIAO, a rotary encoder, a 128x32 OLED display, and powered by Python-based KMK firmware.

## Overall Macropad
![Overall Macropad view of SixPad](path/to/CAD.png)

## Schematic
![Schematic diagram of the SixPad circuit](path/to/Schematic.png)

## PCB Design
![PCB layout of SixPad](path/to/PCB_layout.png)

## Case & Assembly
![Exploded view showing how the case fits together without screws](path/to/case-assembly.png)

## Bill of Materials (BOM)
* **Seeeduino XIAO:** 1x microcontroller
* **Mechanical Switches:** 6x switches
* **Rotary Encoder:** 1x encoder
* **OLED Display:** 1x 128x32 display
* **Case Parts:** 3D-printed Top plate and Bottom tray

## Repository Directory Structure
```text
├── CAD/
│   └── assembly.step
├── PCB/
│   ├── SixPad.kicad_pro
│   ├── SixPad.kicad_sch
│   └── SixPad.kicad_pcb
├── Firmware/
│   └── main.py
└── production/
    ├── Top.STEP
    ├── Bottom.STEP
    ├── gerbers.zip
    └── main.py