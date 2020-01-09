
TEXFILE=VHzQ_MNRAS_rv1
TEXFILE_TWO=PhotometricBands_Conversions
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
#	pdflatex  ${TEXFILE}
#	dvipdf ${TEXFILE}
	rm -f  ${TEXFILE}.aux
	rm -f  ${TEXFILE}.bbl
	rm -f  ${TEXFILE}.blg
	rm -f  ${TEXFILE}.dvi
	rm -f  ${TEXFILE}.log
	rm -f  ${TEXFILE}.out
	rm -f  ${TEXFILE}.toc
#	dvips ERQs_PaperI_rv2.dvi 
#	ps2pdf ERQs_PaperI_rv2.ps
#	rm -f ERQs_PaperI_rv2.ps
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


PhotometricBands :
	pdflatex  ${TEXFILE_TWO}
	pdflatex  ${TEXFILE_TWO}
	bibtex ${TEXFILE_TWO}
	bibtex ${TEXFILE_TWO}
	pdflatex  ${TEXFILE_TWO}
	pdflatex  ${TEXFILE_TWO}
	rm -f  ${TEXFILE_TWO}.aux
	rm -f  ${TEXFILE_TWO}.bbl
	rm -f  ${TEXFILE_TWO}.blg
	rm -f  ${TEXFILE_TWO}.dvi
	rm -f  ${TEXFILE_TWO}.log
	rm -f  ${TEXFILE_TWO}.out
	rm -f  ${TEXFILE_TWO}.toc
	open ${TEXFILE_TWO}.pdf
