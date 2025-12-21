# ============================================================
# Escape Sequences in Python – COMPLETE REVISION WITH EXAMPLES
# ============================================================
#
# Escape sequences are special character combinations
# used inside string literals to represent:
#   - New lines
#   - Tabs
#   - Quotes
#   - Special formatting characters
#
# They always start with a backslash (\)
#
# ============================================================
# COMMON ESCAPE SEQUENCES
# ============================================================
# \n  → New Line
# \t  → Horizontal Tab
# \\  → Backslash
# \'  → Single Quote
# \"  → Double Quote
# \r  → Carriage Return
# \b  → Backspace
# \f  → Form Feed
# \v  → Vertical Tab
# ============================================================


# ============================================================
# 1️⃣ NEW LINE (\n)
# ============================================================
# \n moves the cursor to the next line
print("Hello,\nWorld!")
# Output:
# Hello,
# World!


# ============================================================
# 2️⃣ HORIZONTAL TAB (\t)
# ============================================================
# \t adds spacing similar to pressing the TAB key
print("Column1\tColumn2\tColumn3")
# Output:
# Column1    Column2    Column3


# ============================================================
# 3️⃣ BACKSLASH (\\)
# ============================================================
# To print a single backslash, we must escape it using \\
print("This is a backslash: \\")
# Output:
# This is a backslash: \


# ============================================================
# 4️⃣ SINGLE QUOTE (\')
# ============================================================
# Useful when the string itself is enclosed in single quotes
print('He said, \'Python is fun!\'')
# Output:
# He said, 'Python is fun!'


# ============================================================
# 5️⃣ DOUBLE QUOTE (\")
# ============================================================
# Useful when the string is enclosed in double quotes
print("She replied, \"Indeed it is!\"")
# Output:
# She replied, "Indeed it is!"


# ============================================================
# 6️⃣ CARRIAGE RETURN (\r)
# ============================================================
# \r moves the cursor to the beginning of the same line
# Text after \r overwrites existing text
print("First Line\rSecond Line")
# Output (environment dependent):
# Second Line


# ============================================================
# 7️⃣ BACKSPACE (\b)
# ============================================================
# \b removes the character just before it
print("Hello\bWorld!")
# Explanation:
# "Hello" -> \b removes 'o'
# Result becomes: HellWorld!
# Output:
# HellWorld!


# ============================================================
# 8️⃣ FORM FEED (\f)
# ============================================================
# \f represents a page break
# Mostly used in old printers / documents
print("Page1\fPage2")
# Output may not be visually clear in modern consoles


# ============================================================
# 9️⃣ VERTICAL TAB (\v)
# ============================================================
# \v adds vertical spacing
print("Line1\vLine2")
# Output depends on terminal support


# ============================================================
# IMPORTANT NOTE
# ============================================================
# Escape sequences like \r, \b, \f, and \v
# may NOT show visible effects in all editors or terminals.
# Their behavior depends on the environment.
# ============================================================


# ============================================================
# 🔟 RAW STRINGS (r"")
# ============================================================
# Raw strings treat backslashes as literal characters
# Escape sequences are NOT processed
raw_str = r"C:\Users\Name\Documents"
print(raw_str)
# Output:
# C:\Users\Name\Documents


# ============================================================
# 1️⃣1️⃣ MULTI-LINE STRINGS WITH ESCAPE SEQUENCES
# ============================================================
multi_line_str = (
    "This is line one.\n"
    "This is line two.\n"
    "\tThis line is indented."
)

print(multi_line_str)
# Output:
# This is line one.
# This is line two.
#     This line is indented.


# ============================================================
# 1️⃣2️⃣ COMBINING MULTIPLE ESCAPE SEQUENCES
# ============================================================
combined_str = (
    "Path:\n"
    "\tC:\\Users\\Name\\Documents\n"
    "End of Path"
)

print(combined_str)
# Output:
# Path:
#     C:\Users\Name\Documents
# End of Path


# ============================================================
# FINAL NOTES (REVISION POINTS)
# ============================================================
# ✔ Escape sequences are interpreted inside normal strings
# ✔ Use \\ to print a single backslash
# ✔ Use raw strings (r"...") for file paths and regex
# ✔ Not all escape sequences behave the same in every terminal
# ✔ Raw strings do NOT process escape sequences
# ============================================================
