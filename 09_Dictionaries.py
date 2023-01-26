monthConversions = {
    1: "January",
    2: "Februray",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    "Dec": "December"
}

print(monthConversions[1])
print(monthConversions.get("Dec"))
print(monthConversions.get("Luv"))
print(monthConversions.get("Luv", "Not a valid key"))
