mkdir -p tmp > /dev/null
echo "Created Directory"
pdflatex -output-directory tmp $1.tex > /dev/null
echo "Created PDF"
pdftoppm tmp/$1.pdf tmp/$1 -png > /dev/null
echo "Created PNG"
mv tmp/$1-1.png ./$1.png > /dev/null
# rm -rf tmp > /dev/null