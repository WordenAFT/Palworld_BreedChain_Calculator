# Palworld Breeding Chain Calculator
(Current as of 27 Jan 24, V3)

This Script Calculates a successful breeding path to a target Pal with a specified Inherited Pal (or pals). There can be multiple inherited pals, and excluded pals can also be specified (in the event you don't have the pal!)

<img width="430" alt="image" src="https://github.com/WordenAFT/Palworld_BreedChain_Calculator/assets/37527600/1fc835f5-92c3-41b9-a0f7-536fee27fb32">


The packaged .exe file was >25 MB (~100 mb, so I can't upload it here. If you have ideas on how to do that, let me know!

* When adding pals to the inherited and excluded lists, do not add commas between the pal names.
* The inputs are not case-sensitive. Have at it!

### Limitations
This script also cannot handle special combination target species. I plan to work on this in the next few days and upload a change to allow for it.

Special Combinations (Not currently handled):

`'Relaxaurus Lux', 'Incineram Noct', 'Mau Cryst',
                       'Vanwyrm Cryst','Eikthyrdeer Terra','Elphidran Aqua',
                        'Pyrin Noct','Mammorest Cryst','Mossanda Lux',
                        'Dinossom Lux','Jolthog Cryst','Frostallion Noct',
                    'Kingpaca Cryst','Lyleen Noct','Leezpunk Ignis',
                        'Blazehowl Noct','Robinquill Terra','Broncherry Aqua',
                 'Surfent Terra','Gobfin Ignus','Suzaku Aqua',
                       'Reptyro Cryst','Hangyu Cryst','Lyleen',
                     'Faleris','Grizzbolt','Orserk','Shadowbeak'`

Hope you like it!

## <u> Google Drive Link to Download .exe: </u>

[Google Drive Link](https://drive.google.com/file/d/14RuhLwh1cPLan1hxQsd55XGBmW-VJiEr/view?usp=drive_link "Click here to download")



### Notes on the Download (Why in the world.... is it 297MB??)

I am an absolute amateur with packaging python scripts into a .exe. This script uses Tkinter for the GUI and Pyinstaller to package, which resulted in a final file size of 297MB. This is grossly bloated since the two scripts i developed for this project total approximately 15 kb. If you have ideas on how I can package this in a much smaller format, please let me know!
