from datetime import date

def calculate_age(born):
  today = date.today()
  return today.year - born
