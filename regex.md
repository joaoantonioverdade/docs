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
\\          | escape character




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


TODO: Anchors, boundaries, inline modifiers, lookarounds


# References

[Rexegg](http://www.rexegg.com/)