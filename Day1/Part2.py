

data = open("Day1data.txt", "r")
masses = data.readlines()



def cal_fuel_mass(mass):
    return int(mass/3)-2



def fuelCalc(mass):
  new_fuel = cal_fuel_mass(mass)
  sum_fuel_mass = []
  while  new_fuel > 0:
      sum_fuel_mass.append(new_fuel)
      new_fuel = cal_fuel_mass(sum_fuel_mass[-1])
  return sum(sum_fuel_mass)


def main():
  fuel_sum = 0
  for mass in masses:
      mass = mass.strip()
      fuel_sum += fuelCalc(int(mass))
  return fuel_sum


print(main())