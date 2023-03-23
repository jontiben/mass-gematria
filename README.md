# Mass Gematria
Written by jontiben, 2023

## Usage:
`python mass_gematria.py {target number} {filename}`

**Examples:**

`python mass_gematria.py 666 roman_emperors.txt`

`python mass_gematria.py 47 "C:\Users\jontiben\AppData\Roaming\.minecraft\logs\telemetry\20230204-1.json"`

**Example Output:**

```
MASS GEMATRIA CHECK
Finding words with a value of 59 in file C:\Users\jontiben\Downloads\test_file.txt

Checking gematria systems:
- Ordinal
- Reduction
- Reverse
- Reverse-Reduction

------------------------------------------------

-       cooperation -- Reduction (59)
-       direct -- Ordinal (59)

------------------------------------------------

Finished, 2 total matches.
```

## Behavior:
Files are broken up into segments by spaces and line breaks, and each segment is checked independently for its gematria values. 

Any numbers encountered are considered to have their own value. Punctuation is ignored, even if it appears in the output. There are a number of alternate Latin characters (ø, ð, á, etc.) that are defined in gematria_values.py to be equivalent to one of the 26 standard Latin characters (becoming o, d, a, etc.). This behavior is easily modifiable and extensible by messing with gematria_values.py. Characters that do not appear anywhere in gematria_values.py are ignored. 

Only one instance of a word and the system in which it was matched is shown.

## Supported Gematria Types:
- Ordinal (a=1, b=2, ... z=26)
- Reduction (a=1, b=2, ... i=9, j=1, k=2, ...)
- Reverse(-Ordinal) (a=26, b=25, ... z=1)
- Reverse-Reduction (a=8, b=7, ... h=1, i=9, j=8, ...)

