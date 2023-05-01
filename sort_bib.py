import datetime

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

ref_date = datetime.datetime(1900, 1, 1)

inspire_article_times = {}
for key, entry in inspire_articles.items():
    
    eprint_present = False
    for line in entry[1].splitlines():
        if 'eprint' in line:
            eprint_line = line.strip()
            eprint_present = True
            
    if eprint_present:
        eprint = eprint_line.split('=')[1].strip()[1:-2]
        
        if '.' in eprint:
    
            year = 2000 + int(eprint[:2])
            month = int(eprint[2:4])
            n = int(eprint.split('.')[1])
            
            dt = (datetime.datetime(year, month, 1) - ref_date).days + (n/1e5)
        
        else:
            
            eprint = eprint.split('/')[1]
            
            year = int(eprint[:2])
            if year < 10:
                year = 2000 + year
            else:
                year = 1900 + year
                
            month = int(eprint[2:4])
            n = int(eprint[-3:])
            
            dt = (datetime.datetime(year, month, 1) - ref_date).days + (n/1e3)
            
    else:
        
        year = int(key.split(':')[1][:4])
        dt = (datetime.datetime(year, 1, 1) - ref_date).days 
            
    inspire_article_times[key] = dt
        
inspire_articles_keys = list(inspire_articles.keys())
inspire_articles_keys.sort(key=lambda x: inspire_article_times[x])

# keys.sort(key = lambda x: int(x[x.index(':')+1:x.index(':')+5]))

# Construct the output bib file
bib_out = ''        

# INSPIRE articles

bib_out += '%%%%%%%%%%%%%%%%\n%%% ARTICLES %%%\n%%%%%%%%%%%%%%%%\n\n'

for key in inspire_articles_keys:
    bib_out += inspire_articles[key][1] + '\n\n'
        
# Other articles

bib_out += '%%%%%%%%%%%%%%%%%%%%%%\n%%% OTHER ARTICLES %%%\n%%%%%%%%%%%%%%%%%%%%%%\n\n'

for key, value in other_articles.items():
    bib_out += value[1] + '\n\n'
        
# Books

bib_out += '%%%%%%%%%%%%%\n%%% BOOKS %%%\n%%%%%%%%%%%%%\n\n'

for key, value in books.items():
    bib_out += value[1] + '\n\n'
        
# Misc

bib_out += '%%%%%%%%%%%%%\n%%% OTHER %%%\n%%%%%%%%%%%%%\n\n'

for key, value in misc.items():
    bib_out += value[1] + '\n\n'

bib_out = bib_out.replace('\t', '    ')

# Save to file
with open('bibliography_sorted.bib', 'w') as f:
    f.write(bib_out)
