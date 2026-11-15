# Mission 5 — Numbers and data

## 1. Task / objective
The objective of Mission 5 was to explore how low-level data is encoded and manipulated inside digital computers. This entailed manually calculating base conversions between decimal (base 10), binary (base 2), and hexadecimal (base 16), programmatically verifying the conversions using Python, engineering an interactive CLI number converter (`number_converter.py`), and analyzing text encoding schemes such as ASCII and UTF-8.

---

## 2. Work completed

### Task 5.1 — Convert numbers by hand

#### 1. Convert decimal 13 to binary
- **Method**: Successive integer division by 2, recording remainders:
  - $13 \div 2 = 6$ remainder **1** (LSB)
  - $6 \div 2 = 3$ remainder **0**
  - $3 \div 2 = 1$ remainder **1**
  - $1 \div 2 = 0$ remainder **1** (MSB)
- Read remainders from bottom to top: **$1101_2$**

#### 2. Convert decimal 25 to binary
- **Method**: Successive integer division by 2, recording remainders:
  - $25 \div 2 = 12$ remainder **1** (LSB)
  - $12 \div 2 = 6$ remainder **0**
  - $6 \div 2 = 3$ remainder **0**
  - $3 \div 2 = 1$ remainder **1**
  - $1 \div 2 = 0$ remainder **1** (MSB)
- Read remainders from bottom to top: **$11001_2$**

#### 3. Convert binary 1010 to decimal
- **Method**: Positional expansion using powers of 2:
  - Bit positions: $1 \times 2^3 + 0 \times 2^2 + 1 \times 2^1 + 0 \times 2^0$
  - $= (1 \times 8) + (0 \times 4) + (1 \times 2) + (0 \times 1)$
  - $= 8 + 0 + 2 + 0 = \mathbf{10_{10}}$

#### 4. Convert binary 1101 to decimal
- **Method**: Positional expansion using powers of 2:
  - Bit positions: $1 \times 2^3 + 1 \times 2^2 + 0 \times 2^1 + 1 \times 2^0$
  - $= (1 \times 8) + (1 \times 4) + (0 \times 2) + (1 \times 1)$
  - $= 8 + 4 + 0 + 1 = \mathbf{13_{10}}$

#### 5. Convert hexadecimal A to decimal
- **Method**: In hexadecimal base 16, digits 0–9 represent values 0–9, and letters A–F represent values 10–15.
  - $\text{A}_{16} = 10 \times 16^0 = 10 \times 1 = \mathbf{10_{10}}$

#### 6. Convert hexadecimal 1F to decimal
- **Method**: Positional expansion using powers of 16:
  - $(1 \times 16^1) + (\text{F} \times 16^0)$
  - Since $\text{F} = 15$:
  - $= (1 \times 16) + (15 \times 1) = 16 + 15 = \mathbf{31_{10}}$

#### 7. Convert binary 1111 to hexadecimal
- **Method**: Direct 4-bit nibble mapping:
  - $1111_2 = (1 \times 8) + (1 \times 4) + (1 \times 2) + (1 \times 1) = 15_{10}$
  - In base 16, the decimal value 15 corresponds directly to digit **$\text{F}_{16}$** (or `0xF`).

---

### Task 5.2 — Verify using Python
I opened the interactive Python shell (`python3`) to test and verify every manual conversion from Task 5.1.

| Question / Conversion | Expression Tested | Python Shell Result | Matches Manual Calculation? |
| :--- | :--- | :--- | :--- |
| Decimal 13 to binary | `bin(13)` | `'0b1101'` | **Yes** |
| Decimal 25 to binary | `bin(25)` | `'0b11001'` | **Yes** |
| Binary 1010 to decimal | `int('1010', 2)` | `10` | **Yes** |
| Binary 1101 to decimal | `int('1101', 2)` | `13` | **Yes** |
| Hexadecimal A to decimal | `int('A', 16)` | `10` | **Yes** |
| Hexadecimal 1F to decimal | `int('1F', 16)` | `31` | **Yes** |
| Binary 1111 to hexadecimal | `hex(0b1111)` | `'0xf'` | **Yes** |

---

### Task 5.3 — Build a small number converter
I implemented the interactive converter in `mission-05-numbers-data/number_converter.py`. The program prompts the user for a decimal integer, parses the input, and calculates its binary and hexadecimal representations using Python's built-in functions.

#### Execution and Test Results:

| Test Number (Decimal) | Binary Output (`bin()`) | Hexadecimal Output (`hex()`) |
| :--- | :--- | :--- |
| **42** | `0b101010` (raw: `101010`) | `0x2A` |
| **255** | `0b11111111` (raw: `11111111`) | `0xFF` |
| **8065** *(USN digits)* | `0b1111110000001` | `0x1F81` |

#### Explanation of built-in functions:
- `int(string_input)`: Converts the raw textual string received from `input()` into a base-10 numerical integer stored in memory.
- `bin(integer)`: Takes an integer value and generates a binary representation string prefixed with `'0b'`, which signals that base 2 is being used.
- `hex(integer)`: Takes an integer value and generates a hexadecimal representation string prefixed with `'0x'`, which signals that base 16 is being used.

---

### Task 5.4 — How is text stored?

#### 1. ASCII Decimal Codes:
- **Uppercase letter 'A'**: Decimal code **65** (Binary: `01000001`, Hex: `0x41`)
- **Lowercase letter 'a'**: Decimal code **97** (Binary: `01100001`, Hex: `0x61`)
- *Observation*: The difference between lowercase and uppercase is exactly $97 - 65 = 32$ ($2^5$). In binary, toggling only the 6th bit (bit index 5) switches casing effortlessly.

#### 2. Why does a computer need an encoding standard?
Computers are physical electronic devices whose memory chips and buses only manipulate binary electrical voltages (representing 0 and 1); they possess no native awareness of human letters, alphabets, or punctuation. An encoding standard establishes a universal mathematical contract that maps specific numeric values to designated typographic glyphs, ensuring that a string saved on one machine will be interpreted and rendered with identical meaning on any other system in the world.

#### 3. Example of a character not part of basic ASCII:
The **Indian Rupee symbol (`₹`)** (Unicode code point `U+20B9`). Basic ASCII is a 7-bit encoding standard limited strictly to values 0 through 127, covering the English Latin alphabet, Arabic numerals, and standard typewriter punctuation. Because the Rupee symbol and characters in non-Latin scripts (e.g. Devanagari, Japanese Kanji, emojis) require values well beyond 127, they are encoded using multi-byte standards such as **UTF-8**, where `₹` is stored as a 3-byte sequence (`0xE2 0x82 0xB9`).

---

## 3. Commands / tools used
- Positional arithmetic and successive division algorithms for manual base math.
- `python3`: Launched interactive REPL for verifying binary and hex expressions.
- `number_converter.py`: Developed a CLI conversion program utilizing `input()`, `int()`, `bin()`, and `hex()`.
- Terminal pipe tests: Automated standard input testing with sample values (`42`, `255`, `8065`).

## 4. My understanding
Data representation is the bridge between physical hardware and human abstractions. To the CPU, an integer, a floating-point number, an ASCII character, or a machine instruction are all indistinguishable sequences of 8-bit bytes in memory. It is purely the contextual encoding applied by software that dictates whether byte `01000001` is rendered as the letter "A" or treated as the integer 65. Hexadecimal is particularly useful to developers because exactly 4 binary bits (a nibble) collapse into a single hexadecimal character, making long binary strings like `11111111` readable and concise as `0xFF`.

## 5. Difficulties faced
When accepting user input in Python, forgetting that `input()` always returns a `str` initially meant passing a string to `bin()` would throw a `TypeError: 'str' object cannot be interpreted as an integer`.

## 6. How I resolved them
I wrapped the user input in `int(user_input)` with a `try...except ValueError` block to validate that the user typed numeric digits before passing the integer to `bin()` and `hex()`.

## 7. Evidence / files
- `mission-05-numbers-data/number_converter.py`
- `mission-05-numbers-data/README.md` (this report)

## 8. Commit details
- **Commit Message**: `Build number converter and practise data representation`
- **Pushed to Remote**: Branch `main` on `saksham1319/digital-detective-8065`.
