def roman(num):
  # dictionary with numbers and roman letters
  rom = {1: "I",
         2: "II",
         3: "III",
         4: "IV",
         5: "V",
         6: "VI",
         7: "VII",
         8: "VIII",
         9: "IX",
         10: "X",
         50: "L",
         100: "C",
         500: "D",
         1000: "M"}

  # check if the number is between 10 and 20
  if 10 < num < 20:
    digit = [int(x) for x in str(num)]
    return "X" + rom[digit[1]]
  # check if the number is above/equal 50
  elif num >= 50:
    return rom[num]
  # check if the number is below/equal 10
  elif num <= 10:
    return rom[num]

def test_rom():
  assert roman(9) == "IX"


test_rom()
