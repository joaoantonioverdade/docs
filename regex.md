# Regular Expressions

Characters  | Feature
------------|--------------
\\d         | digit from 0 to 9
\\D         | character not digit
\\w         | word character
\\W         | character not word character
\\s         | white space, tab, newline, carriage return, vertical tab
\\S         | character not a whitespace character
\\t         | tab
\\r         | carriage return
\\b         | word boundary
\\          | escape character

Anchor      | Feature
------------|--------------
\^          | start of string
$           | end of string

Lookarounds | Feature               | Example            | Match
------------|-----------------------|--------------------|-------------------
\(?=...)    | Positive lookahead    | \(?=\d{10})\d{5}   | 01234in0**1234**56789
\(?<=...)   | Positive lookbehind   | \(?<=\d)cat        | cat in 1**cat**
\(?!...)    | Negative lookahead    | \(?!theatre)the\w+ | theme
\(?<!...)   | Negative lookbehind   | \\w{3}(?<!mon)ster | Munster


Quantifiers | Feature
------------|--------------
\*          | zero or more times
?           | once or none
\+          | one or more
{n}         | n times
{n,m}       | n or m times
{n,}        | n or more times



Classes     | Feature
------------|--------------
\[...]      | one of the characters in the brackets
\[^xy]      | one character not x or y



Logic       | Feature         | Example      | Match
------------|-----------------|--------------|------------
\|          | or              | ab|ba        | ab, ba
\(...)      | group           | d(og|oll)    | dog, doll
\\1         | content group 1 | d(o)\\1m     | doo,
\\2         | content group 2 | (a)(b)\\2\\1 | abba
\\(?: ...)  | non-group       | d(?:og)      | dog


# References

[Rexegg](http://www.rexegg.com/)
