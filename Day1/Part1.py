import math
data = open("Day1data.txt", "r")
masses = data.readlines()

# print(masses)

def fuelCalc(fuel_mass):
  fuel_mass = int(fuel_mass/3)-2
  if fuel_mass > 2:
      # won't work, you are adding to fuel mass, it will always be bigger than 2?
      sum_fuel_mass =+ fuel_mass
      fuelCalc(int(fuel_mass))
  return sum_fuel_mass



      

def main():
  fuel_sum = 0
  for mass in masses:
      mass = mass.strip()
      fuel_sum += fuelCalc(int(mass))
  return fuel_sum














