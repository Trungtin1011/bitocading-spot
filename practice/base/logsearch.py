logs = [
  '10.123.45.67 - - [28/Feb/2025:16:24:06 +0700] "GET /auth/login HTTP/1.1" 200 "Login successfully" "Frontend service"',
  '10.123.46.80 - - [28/Feb/2025:16:24:36 +0700] "GET /login HTTP/1.1" 301 "Service moved permanently" "Frontend service"',
  '10.123.45.68 - - [28/Feb/2025:16:25:06 +0700] "GET /auth/login HTTP/1.1" 200 "Login successfully" "Frontend service"',
  '10.123.45.69 - - [28/Feb/2025:16:26:06 +0700] "GET /auth/login HTTP/1.1" 503 "Service unavailable" "Frontend service"',
  '10.123.45.70 - - [28/Feb/2025:16:27:06 +0700] "GET /auth/login HTTP/1.1" 404 "Service not found" "Frontend service"',
]

import re

def check_error(log):
  regex = r"\s(\d{3})\s"
  if re.findall(regex, log)[0] > "200":
    return 1
  return 0

def filter_error(logs):
  for log in logs:
    if check_error(log) == 1:
      print(log)
    else:
      continue

def format_error(logs):
  for log in logs:
    if check_error(log) == 1:
      match = re.match(r'(\S+) - - (\[.*?\]) (".*?") (\d+) "(.*?)" "(.*?)"', log)
      if match:
        print(f"{match.group(6)} - IP: {match.group(1)} - Operation: {match.group(3)} - Message: {match.group(5)}")
      else:
          print("No match found.")

filter_error(logs)
format_error(logs)
