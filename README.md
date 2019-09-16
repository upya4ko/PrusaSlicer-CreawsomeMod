# PrusaSlicer - CreawsomeMod port

*Tested on PrusaSlicer 2.1.0-rc*   
*This port based on [CreawsomeMod for Cura](https://github.com/trouch/CreawsomeMod)*     
*Important: my printer have some modifications to improve print quality and silence, see Recommended upgrades*   

---

## Recommended upgrades:
  * [Fresh marlin with enabled thermal runaway](https://www.youtube.com/watch?v=fIl5X2ffdyo) - safety first!
  * ["Ultrabase like" glass](https://www.creality3d.shop/collections/accessories/products/upgrade-silicon-carbon-ender-3-build-surface-tempered-glass-plate-with-special-chemical-coating-235x235x3mm-for-mk2-mk3-hot-bed) - it incredible, just try and forget about glue and scraper.
  * [TL smoothers](https://ru.aliexpress.com/item/32810007015.html?spm=a2g0s.9042311.0.0.274233edxACo5q) to all steppers - remove salmon skin.
  * [NEMA 17 Steel and Rubber Stepper Motor Vibration Damper](https://ru.aliexpress.com/wholesale?catId=0&initiative_id=SB_20190915034629&SearchText=NEMA+17+Vibration+Damper&switch_new_app=y) - reduce noice.
  * Thermal box - need to ptint ABS and HIPS.
  * [Hero Me Fanduct](https://www.thingiverse.com/thing:3092044) - better cooling with 5015 fan.
  * [Better springs 0.8x0.4x2cm(0.3x0.160.8inch)(ODxIDxL)](https://ru.aliexpress.com/item/32991429216.html?spm=a2g0s.9042311.0.0.274233ed0rkQdU) - hold bed leveling much longer.
  * [Octoprint](https://www.youtube.com/watch?v=SvZjNSLXAJc) - if you want send job to printer in 2 clicks, must have if you print small parts one by one (prototyping).
  * [USB bitrate increase](https://www.thingiverse.com/thing:3626658?fbclid=IwAR1aeB2u3cLCRprocxgbzeCFYMaBGLWcW7z47T3M9EzIA6kJ9vJYJn1P2YE) - need to fix [zits and blobs](https://www.facebook.com/groups/Ender3/permalink/715827812187645/) when printing from octoprint or PC using USB.

## Supported printers:
  * Ender 3   

## Available profiles:
  * 0.12_Super_Quality   
  * 0.20_Standard_Quality   
  * 0.28_Low_Quality   
  * Stupid_Fast_0.28_Low_Quality   
  * Vase_0.12_Super_Quality   
  * Vase_0.28_Low_Quality
  * Gears_0.20_Standard_Quality
  
## Available materials:
  * PLA   
  * ABS
  * ABS Hi-Temp
  * PETg
  * HIPS   
---

## How to install this mod:
### For Windows:
  1. Clone repo or download as ZIP
  2. Copy **printer/\*** to **%appdata%\PrusaSlicer\printer\\**
  3. Copy **filament/\*** to **%appdata%\PrusaSlicer\filament\\**   
  4. Copy **print/\*** to **%appdata%\PrusaSlicer\print\\**   
  5. Select new profile for printer 
  6. Select new profile for filament   
  7. Select new profile for print 
  

### For Linux:
  * Not complete...

---

## Post-processing script:      
By default PrusaSlicer move printhead to first layer height and then move to print start position,
it may scratch print bed or smash paper clips that holding glass, to avoid this problem need combine
first Z and fist X Y move.

Wat do file **PrusaSlicer_post-processing.py** ?    
It move first Z move to first X Y move.   

Script written on Python and tested on Windows 10 and Debian Linux.

Before:
```gcode
M82 ; use absolute distances for extrusion
G92 E0
G1 Z0.200 F7800.000      ; <<<<<<<<<<<<<<<<<<<   
G1 E-3.00000 F2400.00000
G92 E0
G1 X79.973 Y100.228 F7800.000  ; <<<<<<<<<<<<<<<<<<
G1 E3.00000 F2400.00000
G1 F1800
G1 X81.120 Y99.099 E3.04778
G1 X81.978 Y98.511 E3.07866
```

After:
```gcode
M82 ; use absolute distances for extrusion
G92 E0
; Z moved to first X move   ; <<<<<<<<<<<<<<<<<<<<<<<<<<
G1 E-3.00000 F2400.00000
G92 E0
; Combine Z and XY move
G1 X79.973 Y100.228 F7800.000 Z0.2 ; <<<<<<<<<<<<<<<<<<<
; ----------------------
G1 E3.00000 F2400.00000
G1 F1800
G1 X81.120 Y99.099 E3.04778
G1 X81.978 Y98.511 E3.07866
```

---

### How to install **PrusaSlicer_post-processing.py**:
#### For Windows:   
Download [Python for Windows](https://www.python.org/ftp/python/3.6.1/python-3.6.1-embed-win32.zip) 
and extract python.exe to any location.   

Download [**PrusaSlicer_post-processing.py**](https://github.com/McPcholkin/PrusaSlicer-CreawsomeMod/raw/master/post-processing/PrusaSlicer_post-processing.py) to any location.   

Add line to *Print Settings > Output options > Post-processing scripts*
```
D:\Programs\python36.exe D:\Programs\PrusaSlicer\post-processing\PrusaSlicer_post-processing.py;
```
#### For Linux:   
Not complete...
