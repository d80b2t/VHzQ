
TEXFILE=VHzQ_arXiv_submitted
default: all

# just run it

bib: 
	bibtex ${TEXFILE}

all :
	pdflatex  ${TEXFILE}
	pdflatex  ${TEXFILE}
	bibtex ${TEXFILE}
	bibtex ${TEXFILE}
	bibtex ${TEXFILE}
	pdflatex  ${TEXFILE}
	pdflatex  ${TEXFILE}
	rm -f  ${TEXFILE}.aux
#	rm -f  ${TEXFILE}.bbl
	rm -f  ${TEXFILE}.blg
	rm -f  ${TEXFILE}.dvi
	rm -f  ${TEXFILE}.log
	rm -f  ${TEXFILE}.out
	rm -f  ${TEXFILE}.toc

	open ${TEXFILE}.pdf

tect :
	tectonic ${TEXFILE}.tex
	open ${TEXFILE}.pdf


clean:
	rm -f \
	${TEXFILE}.dvi \
	${TEXFILE}.ps \
	${TEXFILE}.out \
	${TEXFILE}.aux \
	${TEXFILE}.bbl \
	${TEXFILE}.blg \
	${TEXFILE}.toc \
	${TEXFILE}.log 
#	${TEXFILE}.pdf



