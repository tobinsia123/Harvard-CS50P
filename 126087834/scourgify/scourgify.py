import csv
import sys
if (len(sys.argv)<3):
    sys.exit("Too few command-line arguments")

elif (len(sys.argv)>3):
    sys.exit("Too many command-line arguments")

else:
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last" ,"house": "house"})
        
        try:
            with open(sys.argv[1],"r") as file:
                    reader=csv.DictReader(file)

                    for row in reader:
                            n1,n2=row["name"].split(",")
                            house=row["house"]
                            writer.writerow({"first": n2.lstrip(), "last": n1 ,"house": house})

        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")

