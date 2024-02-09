from pan import pan

# PAN card number
pan_number = "AAETS9822J"

# PAN object
p = pan.get(AAETS9822J)

# Print PAN details
if p:
    print("PAN Number:", p.number)
    print("Name:", p.name)
    print("Father's Name:", p.father_name)
    print("Date of Birth:", p.dob)
    print("Status:", p.status)
    print("Jurisdiction:", p.jurisdiction)
else:
    print("PAN number not found or invalid.")
