def timeConversion(s):
    # Extract the hour value from the input string
    h = int(s[:2])
    # Extract the "AM" or "PM" suffix from the input string
    p = s[-2:]
    
    # Convert the hour value to a 24-hour value if necessary, based on the suffix
    if p[0]=='P' and h != 12 :
        h+=12
    elif p[0]=='A' and h==12:
        h= 0
    
    # Format the hour value and the rest of the time string as a 24-hour time string
    return f'{h:02d}{s[2:-2]}'    
