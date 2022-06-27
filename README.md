# pp-textX-miniPython

Mini python kompajler, u textX-u

Pre pokretanja aplikacije, potebno je skinuti textX, kao i textX[cli].

U konzoli se unose sledece komande:
	- za proveru ispravnosti gramatike: textx check parser.tx 
	- za proveru python fajla fajl.py u skladu sa gramatikom (leksicka i sintaksna analiza):  textx check fajl.py --grammar parser.tx
	- za pokretanje semanticke analize: 
		1. Pozicionirati se u venv/Scripts folder u konzoli i izvrsiti komadu 'activate'
		2. Pozicionirati se u pocetni forlder textXProject sa komandom 'cd putanja'
		3. Pokrenuti parser: 'python model.py test-fajl.py'



