import re


def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False

    for line in lines:

        line = parse_header_tags(line)

        m = re.match(r'\* (.*)', line)
        if m:
            line = m.group(1)
            if not in_list:
                in_list = True

                line = parse_underscore_markers(line)
                line = '<ul><li>' + line + '</li>'
            else:
                line = parse_underscore_markers(line)
                line = '<li>' + line + '</li>'
        else:
            if in_list:
                in_list_append = True
                in_list = False

        m = re.match('<h|<ul|<p|<li', line)
        if not m:
            line = '<p>' + line + '</p>'

        line = parse_underscore_markers(line)

        if in_list_append:
            line = '</ul>' + line
            in_list_append = False
        res += line
    if in_list:
        res += '</ul>'

    return res


def parse_header_tags(line):
    """ Parse for Hashes '#' denoting Header Tag

    :param line: String list input to be parsed
    :return line: Search (and possibly Replaced) line

    Searches each line (using Regex) to match 6 or less hashes, denoting a header tag.
    Replaces / replays the remaining text. Places a Tag close at end of line.
    """
    match = re.match('^(#+) (.*)', line)
    if match:
        hash_count = match.group(1).count('#')

        if hash_count < 7:
            line = '<h' + str(hash_count) + '>' + match.group(2) + '</h' + str(hash_count) + '>'

    return line


def parse_underscore_markers(line):
    """ Parse Input for bold underscore markers.

    :param line: String list input to be parsed
    :return line: Search (and possibly Replaced) line

    Search and replace inout line, for underscore markers denoting bold,
    or Italics.
    """
    match = re.match('(.*)[_]{2}(.*)[_]{2}(.*)', line)
    if match:
        tag_prefix = 'strong'
        line = match.group(1) + '<' + tag_prefix + '>' + match.group(2) + '</' + tag_prefix + '>' + match.group(3)

    match = re.match('(.*)[_](.*)[_](.*)', line)
    if match:
        tag_prefix = 'em'
        line = match.group(1) + '<' + tag_prefix + '>' + match.group(2) + '</' + tag_prefix + '>' + match.group(3)

    return line
