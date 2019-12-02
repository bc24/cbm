'''
Aufgabe 1
1)	Analysiere die "csv" Datei. 
Summiere für jeden Tag die Anzahl der Zugriffe(flows) und schreibe diese dann im Format
Datum, Summe
in eine neue "csv" Datei

Zur Bearbeitung dieses Datensatzes ist die Datei cs448b_ipasn.csv erforderlich. erforderlich.

Bedeutung der Einträge ( Quelle: http://statweb.stanford.edu/~sabatti/data.html )

Each row consists of four columns: 
•	date: yyyy-mm-dd (from 2006-07-01 through 2006-09-30) 
•	l_ipn: local IP (coded as an integer from 0-9) 
•	r_asn: remote ASN (an integer which identifies the remote ISP) 
•	f: flows (count of connnections for that day) 
'''
Datei=open("./Datasets/cs448b_ipasn.csv","r")
csvdict={}
csv=Datei.readlines()
csv.pop(0)

for i in csv:
    i=i.replace("\n","")
    i=i.split(",")
    
    date=i[0]
    flows=i[3]
    
    if date not in csvdict.keys():
        csvdict[date]=int(flows)
    else:
        csvdict[date]+=int(flows)
print(csvdict)
