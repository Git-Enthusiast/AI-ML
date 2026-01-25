import sys
sys.stdout.reconfigure(encoding='utf-8')

# 
# ============================================================
#               ENCODING IN PYTHON 
# ============================================================
# Encoding is the process of converting data from
# Human Readable Format ➜ Machine Readable Format
# (i.e., Binary form: 0s and 1s)
#
# ➤ The logic or program that performs this conversion
#   is called an ENCODING SYSTEM.
#
# ➤ Encoding helps in:
#   - Efficient storage
#   - Data transmission
#   - Standardized text representation across systems
# ============================================================


# ============================================================
# COMMON ENCODING SYSTEMS
# ============================================================
# ASCII   → Old, limited characters
# UTF-8   → Most widely used encoding today (Web standard)
# UTF-16  → Used by many operating systems
# UTF-32  → Fixed-length, memory-heavy
#
# NOTE:
# Python internally uses Unicode
# ============================================================


# ============================================================
# TOPICS COVERED IN THIS FILE
# ============================================================
# 1️⃣ ASCII Encoding System
# 2️⃣ Unicode Encoding System
# 3️⃣ Unicode Code Points & \U escape sequence
# 4️⃣ ord() and chr() functions
# ============================================================


# ============================================================
# 1️⃣ ASCII ENCODING SYSTEM
# ============================================================
# ASCII = American Standard Code for Information Interchange
#
# ➤ Uses ONLY 7 bits
# ➤ Total characters = 2⁷ = 128
#
# ASCII Character Categories:
# - 33 Control Characters (0–31, 127) → Non-printable
# - 95 Printable Characters
#   - Alphabets
#   - Digits
#   - Punctuation
#   - Special symbols
# ============================================================


# ------------------------------------------------------------
# ASCII VALUE EXAMPLES USING ord()
# ------------------------------------------------------------
print("ASCII value of 'A':", ord('A'))    # 65
print("ASCII value of 'a':", ord('a'))    # 97
print("ASCII value of '0':", ord('0'))    # 48
print("ASCII value of '#':", ord('#'))    # 35


# ------------------------------------------------------------
# ASCII VALUE RANGES (VERY IMPORTANT)
# ------------------------------------------------------------
# Uppercase Letters : 65 – 90   → A–Z
# Lowercase Letters : 97 – 122  → a–z
# Digits            : 48 – 57   → 0–9
#
# Punctuation & Special Symbols:
# 32–47, 58–64, 91–96, 123–126
# ------------------------------------------------------------


# ============================================================
# ASCII PUNCTUATION & SPECIAL CHARACTERS (DETAILED)
# ============================================================

# 🔸 ASCII 32–47
# 32  Space
# 33  !
# 34  "
# 35  #
# 36  $
# 37  %
# 38  &
# 39  '
# 40  (
# 41  )
# 42  *
# 43  +
# 44  ,
# 45  -
# 46  .
# 47  /

# 🔸 ASCII 58–64
# 58  :
# 59  ;
# 60  <
# 61  =
# 62  >
# 63  ?
# 64  @

# 🔸 ASCII 91–96
# 91  [
# 92  \
# 93  ]
# 94  ^
# 95  _
# 96  `

# 🔸 ASCII 123–126
# 123 {
# 124 |
# 125 }
# 126 ~


# ============================================================
# 2️⃣ UNICODE ENCODING SYSTEM
# ============================================================
# Unicode is a UNIVERSAL character encoding standard.
#
# ➤ Supports text from:
#   - All languages
#   - Emojis
#   - Symbols
#   - Mathematical notations
#
# ➤ Can represent more than 1,000,000 characters
# ============================================================


# ============================================================
# UNICODE CODE POINTS
# ============================================================
# Each Unicode character has a unique NUMBER
# called a Unicode Code Point.
#
# Format:
#   U+XXXX  (Hexadecimal)
#
# Example:
#   'A' → U+0041
# ============================================================


# ============================================================
# 3️⃣ UNICODE IN PYTHON (\U ESCAPE SEQUENCE)
# ============================================================
# Python allows Unicode characters using:
#
# \UXXXXXXXX  → 8-digit hexadecimal number
# ============================================================

# Unicode for 'A'
print("\U00000041")     # Output: A

# Explanation:
# Character  : A
# Unicode CP : U+0041
# Hex Value  : 00000041
# Decimal   : 65
# ASCII     : 65

# Unicode for Emoji 😊
print("\U0001F60A")     # Output: 😊


# ============================================================
# 4️⃣ ord() AND chr() FUNCTIONS
# ============================================================
# ord(character)
# ➤ Converts character ➜ Unicode Code Point (Integer)
#
# chr(number)
# ➤ Converts Unicode Code Point ➜ Character
# ============================================================


# ------------------------------------------------------------
# ord() EXAMPLES
# ------------------------------------------------------------
print("Unicode of 'A':", ord('A'))        # 65
print("Unicode of 'a':", ord('a'))        # 97
print("Unicode of '😊':", ord('😊'))      # 128522


# ------------------------------------------------------------
# chr() EXAMPLES
# ------------------------------------------------------------
print("Character of 65:", chr(65))            # A
print("Character of 97:", chr(97))            # a
print("Character of 128522:", chr(128522))    # 😊


# ============================================================
# UNICODE ENCODING FORMATS
# ============================================================
# UTF-8   → 1 byte (8 bits)   → Most common (Web standard)
# UTF-16  → 2 bytes (16 bits)
# UTF-32  → 4 bytes (32 bits)
# ============================================================


# ============================================================
# IMPORTANT NOTE (EXAM + INTERVIEW)
# ============================================================
# ✔ Python supports ASCII as a SUBSET of Unicode
# ✔ ASCII values are SAME in Unicode
# ✔ Unicode is backward compatible with ASCII
# ============================================================
