import requests

zone=sys.argv[1]
origin = (str(input("What is the origin domain?\n")))
originDot = (origin+".")
dotOrigindot = ("."+origin+".")
print("Here is your fixed zone:\n\n")
if "ORIGIN" not in zone:
    print ("$ORIGIN "+origin)
fh = open(zone)
for line in fh:
    if ";" in line:
        continue
    if "ORIGIN" not in line:
        removeDomain1 = line.replace(dotOrigindot, "")
        removeDomain2 = removeDomain1.replace(originDot, "@")
        removeDomain3 = removeDomain2.replace(origin, "@")
    else:
        continue
    if "SOA" in line:
        continue
    elif "CNAME" in line:
        recordType="CNAME"
    elif "A" in line:
        recordType="A"
    elif "TXT" in line:
        recordType="TXT"
    elif "SPF" in line:
        recordType="SPF"
    elif "MX" in line:
        recordType="MX"
    elif "CAA" in line:
        recordType="CAA"
    elif "PTR" in line:
        recordType="PTR"
    elif "SRV" in line:
        recordType="SRV"
    elif "NS" in line:
        recordType="NS"
    else:
        recordType="none"
    if (recordType != "none"):
        if "IN" not in line:
            withIn = ("IN\t"+recordType)
            output = removeDomain3.replace(recordType, withIn)
        else:
            output = removeDomain3
    else:
        output = line
    if (recordType == "NS"):
        if "@" in output:
            continue
    if (recordType == "CNAME"):
        if "@" in output:
            print("\033[1;31;40m ERROR: CANNOT HAVE CNAME FOR THE ROOT DOMAIN  \n")
            break
    if (recordType == "SRV"):
        if "@" in output:
            print("\033[1;31;40m ERROR: CANNOT HAVE SRV FOR THE ROOT DOMAIN  \n")
            break
    print(output)