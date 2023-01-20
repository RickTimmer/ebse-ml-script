import re

from formatting import red, color_text

# todo:
#   - remove strings that became empty after preprocessing


reply_patterns = [
    re.compile("On ((Mon|Tue|Wed|Thu|Fri|Sat|Sun), )?"
               "\\d+ (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec) \\d+,? "
               "at \\d+:\\d+, .+ wrote:"),

    re.compile("On (Mon|Tue|Wed|Thu|Fri|Sat|Sun), "
               "(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec) \\d+, "
               "\\d+,? "
               "at \\d+:\\d+ (AM|PM),? .+ wrote:"),



    re.compile("On \\d+/\\d+/\\d+ \\d+:\\d+, .+ wrote:"),
    re.compile(".+ hat am \\d+\\.\\d+\\.\\d+ \\d+:\\d+ geschrieben:"),
    re.compile("From:[\\S\\s]*Date:[\\S\\s]*To:[\\S\\s]*Subject:", re.MULTILINE)
]


def remove_embedded(raw):
    """
    Remove emails that were embedded in another.
    In case one is found, the email affected is printed, as well as the portion removed in red.
    :param raw:
    :return:
    """
    # containing indexes where a pattern's first match started
    matches = []
    raw = ' '.join(raw.split())

    for pattern in reply_patterns:
        match_found = pattern.search(raw)
        if match_found:
            start_of_chain = match_found.span()[0]
            matches.append(start_of_chain)

    if len(matches) > 0:
        start_of_chain = min(matches)  # get the first match in the text
        stripped = raw[: start_of_chain]
        print(stripped + color_text(raw[start_of_chain:], red))
        return stripped

    return raw
