ping -c $1 $2 > pingInfo.txt
grep 'time=' pingInfo.txt | cut -f 8 -d ' ' | cut -f 2 -d '=' > packages.csv
echo "-- Ping Statistics --"
echo "Packets Transmited : "$1
echo "Time Avarage:"
awk '{count=count+$1}END{print count/NR}' packages.csv
