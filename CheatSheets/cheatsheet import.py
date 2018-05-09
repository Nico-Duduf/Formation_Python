#importer un module
import nomDuModule
#utilisation
nomDuModule.fonction()

#changer le nom du module a l'import
import nomDuModule as nM
nM.fonction()

#importer une (ou plusieurs) fonctions seulement
from leModule1 import laFonction
from leModule2 import laFonction1, laFonction2
laFonction()
laFonction1()
laFonction2()
