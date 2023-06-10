bash c.sh $1

while true
do
    watch --chgexit -n 1 "shasum $1.tex | head --bytes 32"
    echo "Rebuild" && bash c.sh $1
done