import csv
import operator

class Error(Exception):
   pass

val_apm_veids = None
vai_atr_pie_ielas = None
velme_redz_nak_rezult = None


print("Programma, kas pēc lietotāja vajadzībām atrod izdevīgākās un pieejamākās bankas, kur apmainīt naudu no EUR uz USD nejuridiskām vajadzībām.\n")

# val_apm_veids = vai lietotājs apmainīs valūtu skaidrā veidā vai caur bankas pārskaitījumu?
while True:
   try: 
      val_apm_veids = int(input("Ievadiet 1, ja jūs apmainīsiet valūtu skaidrā veidā\nIevadiet 2, ja jūs apmainīsiet valūtu caur bankas pārskaitījumu\n"))    
      if val_apm_veids < 1:
         raise Error
      elif val_apm_veids > 2:
         raise Error
      break
   except:
      print("Lūdzu ievadiet 1 vai 2.\n")

# ja lietotājs apmaina val caur skaidru naudu un atrodas Rīgā, vai_atr_pie_ielas = vai lietotājs atrodas tuvumā pie Latvijas Bankas?
if val_apm_veids == 1:
   atr_vieta = input("\nIevadiet jūsu atrašanās vietu\n")
   if atr_vieta.strip().lower() == "rīga" or atr_vieta.strip().lower() == "riga":
      while True:
         try:
            vai_atr_pie_ielas = int(input("\nIevadiet 1, ja jūs atrodaties tuvumā pie K. Valdemāra ielas 2A. Ja neatrodaties, ievadiet 2.\n"))
            if vai_atr_pie_ielas < 1:
               raise Error
            elif vai_atr_pie_ielas > 2:
               raise Error
            break
         except:
            print("Lūdzu ievadiet 1 vai 2.\n")

# ja lietotājs atrodas tuvumā pie Latvijas Bankas, velme_redz_nak_rezult = vai lietotājs vēlas redzēt citas bankas, kur apmainīt naudu? 
if vai_atr_pie_ielas == 1:
   print("\nVispieejamākā vieta, kur apmainīt valūtu ir Latvijas Banka.\n")
   while True:
      try:
         velme_redz_nak_rezult = int(input("Ja jūs vēlaties redzēt citas bankas, kuras būtu izdevīgi apmainīt naudu, ievadiet 1. Ja nevēlaties, ievadiet 2.\n"))
         if velme_redz_nak_rezult < 1:
            raise Error
         elif velme_redz_nak_rezult > 2:
            raise Error
         break
      except:
         print("Lūdzu ievadiet 1 vai 2.\n")
else: # citādāk, ja lietotājs neatrodas tuvumā pie LB, tad ir vēlme redzēt citas bankas, kur apmainīt naudu
   velme_redz_nak_rezult = 1

# ja lietotājs vēlas redzēt banku izdevīguma tabulu (ja lietotājs atrodas pie LB) vai neatrodas pie Latvijas Bankas, tad tā tiek parādīta
if velme_redz_nak_rezult == 1:
   val_kursi = csv.reader(open("val-kursi.csv"), delimiter=",")
   val_kursi_sorted = sorted(val_kursi, key=operator.itemgetter(1), reverse=True) # sakārto datubāzi pēc kursiem augošā secībā
   print("\n  Izdevīgāko banku tabula:")
   for Banka, Kurss in val_kursi_sorted:
      print("{:<21} {:<15}".format(Banka,Kurss))
elif velme_redz_nak_rezult == 2:
   exit()