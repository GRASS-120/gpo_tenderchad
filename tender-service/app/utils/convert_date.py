from datetime import datetime

def convert_date (date_string):
  return datetime.strptime(date_string, "%d.%m.%Y")