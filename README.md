# Slic3rPE - Settings
My configuration for SlicerPE

Print settings for:
  * ABS
  * PLA
  * PETg
  * FLEX
  * HIPS


Post-processing script:    
Wat do file **Slic3r_post_processing.py** ?    
It move first Z move to first X Y move (to avoid scratch bed surface on first move after Home move).   

Script writen on Python and tested on Windows 10 and Debian Linux.

Before:
```gcode
M73 P0 R81
G92 E0    ; Reset extruder to 0 zero end of cleaning run
G1 Z15 F9000    ; lift nozzle
G21 ; set units to millimeters
G90 ; use absolute coordinates
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
M73 P0 R81
G92 E0    ; Reset extruder to 0 zero end of cleaning run
G1 Z15 F9000    ; lift nozzle
G21 ; set units to millimeters
G90 ; use absolute coordinates
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

To enable add this line to *Print Settings > Output options > Post-processing scripts*
```
D:\Programs\python36.exe D:\Programs\Slic3r_post_processing.py;
```
