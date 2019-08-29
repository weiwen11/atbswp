import re


def myStrip(text, bad=' '):
    stripRegex = re.compile(r'^({0})+|({0})+$'.format(bad))
    # print(stripRegex)
    # return stripRegex.findall(text)
    return stripRegex.sub('$', text)


print(myStrip('   spamspamspaabcdspam  '))
print(myStrip('   spamspamspaabcdspam  ', 'spam'))
print(myStrip('spamspamspaabcdspamspam', 'spam'))
