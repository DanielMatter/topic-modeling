mkdir -p tmp > /dev/null
pdflatex -output-directory tmp $1.tex > /dev/null
pdftoppm tmp/$1.pdf tmp/$1 -png > /dev/null
mv tmp/$1-1.png ./$1.png > /dev/null
rm -rf tmp > /dev/null