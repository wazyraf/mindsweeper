    Mindsweeper este un joc ce antreneaza memoria vizuala a utilizatorului, dorind sa inlocuiasca nevoia pentru MemoPlus inaintea sesiunii.
    La deschiderea aplicatiei se deschide main_page-ul. Aici avem 3 butoane principale (ElevatedButtons, liniile 56-72) : Play -> pentru inceperea jocului, Settings -> pentru setari de sunet si tema, Profile -> pentru introducerea username-ului. La pornirea jocului porneste muzica si apare un grid de 5x5 (clasa GenerateGrid catre self.generate_grid()) cu un numar de patratele colorate (in functia generate_grid()) , acestea trebuiesc memorate si reproduse dupa disparitia lor (functia delete_grid()). Acest joc va rula la infinit, trecand de la un nivel la altul, daca nu se aleg 3 patratele gresit. In cazul in care se aleg 3 gresit, se reseteaza.

    Contributii:
    -Ciortan Tudor Alexandru -> Design, Modele si Aranjarea codului
    -Cocor Erwin Gilbert Mario -> Implementarea mesajelor la terminarea nivelului, Variabile pentru culori si tematici, account_page, Numarul de tile-uri
    -Fronea Gabriel -> Stage-ul pentru nivele, Updatarea Gridului, settings_page, Sunet

    Surse de inspiratie: -> baza jocului, ideea: https://www.youtube.com/watch?v=fGnT-9iCfmE , am pornit fundatia de la videoclipul acesta, insa de la minutul 10 am mers pe o idee mai         diferita, fata de cea din video
                        ->https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=undexpand - BingAi pentru documentatie si explicatii
                        ->https://chat.openai.com/ - ChatGpt ai pentru unele erori

    
    •Trebuie instalat framework-ul flet(comanda in consola: pip install flet)

    •Actualizarea stage-ului dupa fiecare nivel: https://chat.openai.com/share/b2a737dd-3f6d-4cfb-b006-ab8a7b3b9cd3

    •flet run main.py -d --> pentru rulare cu hot reload (ajuta in modificarea elementelor UI, fara a porni si opri aplicatia), documentatie: https://flet.dev/docs/guides/python/hot-reload/

    •pentru DropDown --> https://flet.dev/docs/controls/dropdown/

    •pentru introducerea sunetelor --> https://flet.dev/docs/controls/audio/
        am folosit https://ytmp3.nu/CNtD/ pentru a converti videoul in mp3

    •https://flet.dev/docs/ -> intreaga documentatie a framework-ului flet

    •https://github.com/wazyraf/mindsweeper -> GitHub 