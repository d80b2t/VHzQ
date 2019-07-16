xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxx Columns of the catalog xxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
1. no. of the source
2-3. galactic coordinates (degree)
4-5. equatorial coordinates (degree)
6-7. equatorial coordinates (hms, dms)
	calculated from J2000 equatorial coordinates with astropy.coordinates
8. name of source
	as published in the referenced papers
9. class of object (originally from the HMQ catalog, Flesch 2015, 2015PASA...32...10F)
	q - general/not specified
	q_lensed - lensed qsr
	QR - radio source
	QX - X-ray source
10-11. Red and Blue/Green magnitude -- originally from the HMQ catalog, Flesch 2015, 2015PASA...32...10F)
	some entries from PanSTARRS-DR1 (upper limits noted as well)
	+ not in the SDSS footprint
	++ not detected with SDSS 
	(this column is not used in the latest entries)
12-16. ugriz psf magnitudes from SDSS dr12-dr14 (5" search radius)
	originally from sdss dr12 quasar catalog
	(if empty -- no identification by sql database)
17-21. ugriz psf magnitude errors SDSS dr12-dr14 (5" search radius)
22. redshift
23-24. source discovery/redshift reference
25-26. X-ray and Radio counterpart identification name (incomplete)
27. FIRST flux density
	-1 not in the coverage
	* not detected, rms noise
28. NVSS flux density (if not in the FIRST coverage)
	only given if source is not in FIRST covergage
	-1 not in nvss coverage
	0 not detected
29-44. VLBI flux densities from literature (various frequency bands)
	multiple observations/flux densities are noted in the given bands
45. VLBI flux density references
46. notes
