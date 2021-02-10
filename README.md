# FDM Informatika II pratybos
##### Turinys

[Užduotys](#užduotys)<br>
[Užduočių atlikimas naudojant MIF kompiuterius](#mif_kompiuteriai)<br>
[Užduočių atlikimas naudojant asmeninius kompiuterius (Windows)](#asmeniniai_kompiuteriai)<br>
[Užduočių atlikimas be VS Code redaktoriaus](#jupyter_notebook)<br>
[Užduotys pasikartojimui](#užduotys_pasikartojimui)<br>

<a name="užduotys"/>

### Užduotys
#### Atnaujinta
 - [1 užduotis](https://github.com/albertas/fdm2/blob/master/tasks/1_oop.ipynb) (max 1.67 balo) atsiskaityti iki 2021-03-31.
 - [2 užduotis](https://github.com/albertas/fdm2/blob/master/tasks/2_tests.ipynb) (max 1.67 balo) atsiskaityti iki 2021-04-19.
 - [3 užduotis](https://github.com/albertas/fdm2/blob/master/tasks/3_threads.ipynb) (max 1.67 balo) atsiskaityti iki 2021-05-24.

Maksimalus užduoties balas mažinamas po 10% už kiekvieną pavėluotą savaitę atsiskaityti.

Galima gauti papildomą 1 balą už pristatymą pratybų metu. 
 - Pristatymas turi būti susijęs su Python programavimo kalba.
 - Tai gali būti Jūsų asmeninio projekto pristatymas.
 - Tai gali būti Python bibliotekų palyginimas
 - Ar Jums aktulios Python bibliotekos funkcionalumo pristatymas.  

<a name="mif_kompiuteriai"/>

## Užduočių atlikimas naudojant MIF kompiuterius
### Prisijungimas prie MIF kompiuterio
1. Sužinokite savo studento pažymėjimo numerį [lsp.lt](https://lsp.lt) svetainėje, jis taip pat pateiktas ant Jūsų LSP pažymėjimo.
2. Susikurkite savo VU paskyrą: [id.vu.lt](https://id.vu.lt) puslapyje
3. Susikurkite savo MIF paskyrą: [https://radius.mif.vu.lt/passwd2](https://radius.mif.vu.lt/passwd2) puslapyje.
4. Prie MIF kompiuterio galite prisijungti naudodami MIF paskyrą. Prisijungdami pasirinkite:  **linux (vnc)**

### MS Visual Studio Code įsidiegimas
Šis redaktorius jau **turėtų būti įdiegtas**, bet jeigu nėra, atlikite šias instrukcijas:
1. Terminale įvykdydami šias komandas įsidiegsite [MS Visual Studio Code](https://code.visualstudio.com/Download):

```
cd ~/Desktop     # VS Code failai bus atsiųsti ir išsaugoti ant Desktop
wget https://az764295.vo.msecnd.net/stable/ae08d5460b5a45169385ff3fd44208f431992451/code-stable-1580986866.tar.gz
tar -xzvf code-stable-1580986866.tar.gz    # Išskleidžia atsisiųstą failą
ln -s ./VSCode-linux-x64/bin/code ~/Desktop/VS_Code   # Sukuria VS Code nuorodą ant Desktop'o
```

2. Įsidiekite `Python` plėtinį, skirtą MS Visual Studio Code:

![Visual instructions how to intall Python extension](https://raw.githubusercontent.com/albertas/fdm2/master/images/install_python_extension_for_vs_code.gif)

3. Nusiklonuokite užduočių failus, terminale įvykdydami:

```
git clone https://github.com/albertas/fdm2 ~/Desktop/info2
```

4. Atsidarykite užduočių failą, naudodami VS Code:

![Open task file using VS Code](https://raw.githubusercontent.com/albertas/fdm2/master/images/open_task_file.gif)

<a name="asmeniniai_kompiuteriai"/>

## Užduočių atlikimas naudojant asmeninius kompiuterius (Windows)
1. Įsidiekite [Python](https://www.python.org/downloads/). Įsitikinkite, kad
   diegiant yra pasirinkta *Add Python to environement variables*.
2. Įsidiekite [Git bash](https://gitforwindows.org/), atsiųsdami ir įvykdydami
   [Windows Git bash vykdomąjį failą](https://github.com/git-for-windows/git/releases/tag/v2.25.0.windows.1),
   kuris pateiktas puslapio apačioje `assets` skiltyje. Git bash yra Linux Terminalo atitikmuo.
3. Atsidarę Git bash įvykdykite šią komandą, kad būtų įdiegti Python paketai:

```
pip install --user requests jupyter dill
```

4. Įsidiekite [MS Visual Studio Code](https://code.visualstudio.com),
   atsisiųsdami [Windows VS Code vykdomąjį failą](https://code.visualstudio.com/Download) ir jį paleisdami.
5. Įsidiekite `Python` plėtinį, skirtą MS Visual Studio Code:

![Visual instructions how to intall Python extension](https://raw.githubusercontent.com/albertas/fdm2/master/images/install_python_extension_for_vs_code.gif)

6. Nusiklonuokite užduočių failus, Git Bash terminale įvykdydami:

```
git clone https://github.com/albertas/fdm2 ~/Desktop/info2
```

7. Atsidarykite užduočių failą, naudodami VS Code:

![Open task file using VS Code](https://raw.githubusercontent.com/albertas/fdm2/master/images/open_task_file.gif)


<a name="jupyter_notebook"/>

## Užduočių atlikimas be VS Code redaktoriaus Linux aplinkoje:
Terminale įvykdykite komandas:
 1. cd ~/Desktop
 2. git clone https://github.com/albertas/fdm2 ~/Desktop/info2
 3. python3 -m venv venv
 4. venv/bin/pip install wheel dill jupyter requests
 5. venv/bin/jupyter-notebook ~/Desktop/info2/tasks/1_oop.ipynb

## Užduočių atlikimas be VS Code redaktoriaus Windows aplinkoje:
Git Bash terminale įvykdykite komandas:
 1. cd ~/Desktop
 2. git clone https://github.com/albertas/fdm2 ~/Desktop/info2
 3. python -m venv venv
 4. venv/Scripts/pip install wheel dill jupyter requests
 5. venv/Scripts/jupyter-notebook ~/Desktop/info2/tasks/1_oop.ipynb

<a name="užduotys_pasikartojimui"/>

## Užduotys pasikartojimui
Šios užduotys apima viską, ką turėjote išmokti pirmojo (Informatika I) semestro metu:
 1. [Kintamjieji](https://github.com/albertas/fdm2/blob/master/revision_tasks/1_variables.ipynb)
 2. [Sąlygos sakiniai ir ciklai](https://github.com/albertas/fdm2/blob/master/revision_tasks/2_conditions_and_loops.ipynb)
 3. [Funkcijos](https://github.com/albertas/fdm2/blob/master/revision_tasks/3_functions.ipynb)
 4. Darbas su failais

Šios pasikartojimo užduotys yra išsaugotos `~/Desktop/info2/revision_tasks/` kataloge, jas galite atsidaryti ir vykdyti naudodami Visual Studio Code. 
