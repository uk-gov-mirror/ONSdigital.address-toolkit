#########################################################################
# UK POSTCODE REGEX PATTERN
##########################################################################
postcode_regex = r"([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z]\d{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y]\d{1,2})|(([A-Za-z]\d[A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y]\d[A-Za-z]?))))\s?\d[A-Za-z]{2})"

#########################################################################
# UNIT ADDRESS LEVEL REGEX PATTERNS
##########################################################################
flat_regex = r'(?i)((\bFLAT\s((NO|NO\.)\s?)?([-A-Z0-9\.]{1,4}|([^A-Z]{1,6})))\s|\bFLAT[-0-9A-RU-Z\.]{1,4}\s|\bFLAT\s)((\s?-\s?|\s?TO\s|\s?&\s?|\s?\\\s?)((\bFLAT\s)?[-A-Z0-9\.]{1,4}\b)\s)?'
flat_regex_alternative = r"(?i)\b(?:flat|flats)\b[\s\-,:]*[A-|0-9]+(?:[\-\/][A-Z0-9]+)?|\b[A-Z0-9]+(?:[\-\/][A-Z0-9]+)?\s*\b(?:flat|flats)\b"

room_regex = r'(?i)((\bROOM\s((NO|NO\.)\s?)?([-A-Z0-9\.]{1,4}|([^A-Z]{1,6})))\s|\bROOM[-0-9A-RT-Z\.]{1,4}\s|\bROOM\s)((\s?-\s?|\s?TO\s|\s?&\s?|\s?\\\s?)((\bROOM\s)?[-A-Z0-9\.]{1,4}\b)\s)?'
room_regex_alternative = r"(?i)\b(?:room|rooms)\b[\s\-,:]*[A-|0-9]+(?:[\-\/][A-Z0-9]+)?|\b[A-Z0-9]+(?:[\-\/][A-Z0-9]+)?\s*\b(?:room|rooms)\b"

unit_regex = r'(?i)((\bUNIT\s((NO|NO\.)\s?)?([-A-Z0-9\.]{1,4}|([^A-Z]{1,6})))\s|\bUNIT[-0-9A-RT-Z\.]{1,4}\s|\bUNIT\s)((\s?-\s?|\s?TO\s|\s?&\s?|\s?\\\s?)((\bUNIT\s)?[-A-Z0-9\.]{1,4}\b)\s)?'
unit_regex_alternative = r"(?i)\b(?:unit|units)\b[\s\-,:]*[A-|0-9]+(?:[\-\/][A-Z0-9]+)?|\b[A-Z0-9]+(?:[\-\/][A-Z0-9]+)?\s*\b(?:unit|units)\b"

block_regex = r'(?i)((\bBLOCK\s((NO|NO\.)\s?)?([-A-Z0-9\.]{1,4}|([^A-Z]{1,6})))\s|\bBLOCK[-0-9A-RT-Z\.]{1,4}\s|\bBLOCK\s)((\s?-\\s?|\s?TO\s|\s?&\s?\\\s?)((\bBLOCK\s)?[-A-Z0-9\.]{1,4}\b)\s)?'
block_regex_alternative = r"(?i)\b(?:block|blocks)\b[\s\-,:]*[A-|0-9]+(?:[\-\/][A-Z0-9]+)?|\b[A-Z0-9]+(?:[\-\/][A-Z0-9]+)?\s*\b(?:block|blocks)\b"

apartment_regex = r'(?i)((\bAPARTMENT\s((NO|NO\.)\s?)?([-A-Z0-9\.]{1,4}|([^A-Z]{1,6})))\s|\bAPARTMENT[-0-9A-RT-Z\.]{1,4}\s|\bAPARTMENT\s)((\s?-\s?|\s?TO\s|\s?&\s?\\\s?)((\bAPARTMENT\s)?[-A-Z0-9\.]{1,4}\b)\s)?'
apartment_regex_alternative = r"(?i)\b(?:apartment|apartments)\b[\s\-,:]*[A-|0-9]+(?:[\-\/][A-Z0-9]+)?|\b[A-Z0-9]+(?:[\-\/][A-Z0-9]+)?\s*\b(?:apartment|apartments)\b"

floor_regex = r'(?i)BASEMENT|((GROUND|FIRST|SECOND|THIRD|FOURTH|FIFTH|SIXTH|SEVENTH)\sFLOOR\b)'
floor_regex_alternative = r"(?i)\b(basement|ground|bottom|middle|first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|top floor|upper floor|\d+(?:st|nd|rd|th)\s+floor)\b"

#########################################################################
# MISC REGEX PATTERNS
##########################################################################
misc_numbers_regex = r'(^|\s)(\D?(\d+\.\d+(\.\d+)?\.?\s)|([A-Z]{1,2}\d+\s))'
standalone_numbers_regex = r'((^|^\D*\s)\d+(\s?[A-Z]\b)?)((\s?-\s?|\sTO\s|\\|\/|\s)(\d+(\s?[A-Z]\b)?))?(?!.+\b\d)'
txt_before_numbers_regex = r'^\D+\s(?=\d+)'
end_address_numbers_regex = r'((?<=\s)\d+(\s?[A-Z]\b)?)((\s?-\s?|\sTO\s|\\|\/|\s)(\d+(\s?[A-Z]\b)?))?(?!.+(\b\d+(\s?[A-Z]\b)?)((\s?-\s?|\sTO\s|\\|\/|\s)(\d+(\s?[A-Z]\b)?))?)'
start_address_numbers_regex = r'^\d+'
start_address_identifier_regex = r'((?<=^\d{1})|(?<=^\d{2})|(?<=^\d{3})|(?<=^\d{4}))\s?([A-Z]\b)'
end_address_identifier_regex = r'((?<=^\d{1})|(?<=^\d{2})|(?<=^\d{3})|(?<=^\d{4}))(?<=\s)?([A-Z]\b)?(\s?-\s?|\sTO\s|\\|\/|\s)\s?\d+'

#########################################################################
# NOISE REGEX PATTERNS
##########################################################################
consecutive_letters_regex = r"(?i)\b([A-Z])\1{3,}\b"