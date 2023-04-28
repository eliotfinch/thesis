with open('bibliography.bib') as f:
    bib_in = f.read().strip()

# Split bib entries and strip comments
entries_list = [e for e in bib_in.split('\n\n') if e[0] == '@']

# Convert entries list to a dictionary and remove duplicates
entries_dict = {}
for entry in entries_list:
    head = entry.split('\n')[0]
    
    entry_type = head[1:head.index('{')]
    ID = head[head.index('{')+1: -1]
    
    if ID not in entries_dict:
        entries_dict[ID] = (entry_type, entry)
        
# Group entries according to type

inspire_articles = {}
other_articles = {}
books = {}
misc = {}

for key, value in entries_dict.items():
    if (value[0] == 'article') and (':' in key) and ('doi' not in key):
        inspire_articles[key] = value
    elif value[0].lower() == 'article':
        other_articles[key] = value
    elif value[0] == 'book':
        books[key] = value
    else:
        misc[key] = value
        
# Sort inspire articles
# keys.sort(key = lambda x: int(x[x.index(':')+1:x.index(':')+5]))

# Construct the output bib file
bib_out = ''        

# INSPIRE articles

bib_out += '%%%%%%%%%%%%%%%%\n%%% ARTICLES %%%\n%%%%%%%%%%%%%%%%\n\n'

for key, value in entries_dict.items():
    if (value[0] == 'article') and (':' in key):
        bib_out += value[1] + '\n\n'
        
# Other articles

bib_out += '%%%%%%%%%%%%%%%%%%%%%%\n%%% OTHER ARTICLES %%%\n%%%%%%%%%%%%%%%%%%%%%%\n\n'

for key, value in entries_dict.items():
    if (value[0].lower() == 'article') and (':' not in key):
        bib_out += value[1] + '\n\n'
        
# Books

bib_out += '%%%%%%%%%%%%%\n%%% BOOKS %%%\n%%%%%%%%%%%%%\n\n'

for key, value in entries_dict.items():
    if value[0] == 'book':
        bib_out += value[1] + '\n\n'
        
# Misc

bib_out += '%%%%%%%%%%%%%\n%%% OTHER %%%\n%%%%%%%%%%%%%\n\n'

for key, value in entries_dict.items():
    if value[0] in ['dataset', 'software', 'misc']:
        bib_out += value[1] + '\n\n'

bib_out = bib_out.replace('\t', '    ')

# Save to file
with open('bibliography_sorted.bib', 'w') as f:
    f.write(bib_out)
