# Getting known about Current Working Directory.
import os
path = os.getcwd()

print(f"Current Work Directory (cwd) is: {path} ")

import csv #Instruction to import csv library!

# which file we are working with?
data_path = "pokemonPokemonData.csv"

print("Reading file...")

# Open and closing the file (with).
with open(data_path, "rt") as csv_file:
  csv_reader = csv.reader(csv_file) #



  # Read in the headings
  headings = next(csv_reader)
  print(headings)


  # Read in each record
  for row in csv_reader:
    print(row)

print("Done!!!")