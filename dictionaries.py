
month_conversion = {
    "jan": "January",
    "feb": "February",
    "mar": "MArch",
    "apr": "April",
    "may": "May",
    "jun": "June",
    "jul": "July",
    "aug": "August",
    "sep": "September",
    "oct": "October",
    "nov": "November",
    "dec": "December",
}

print(month_conversion["aug"])

print(month_conversion.get("dec"))

print(month_conversion.get("luv", "invalid entry"))
