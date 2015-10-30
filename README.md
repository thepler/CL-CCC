# CenturyLink Cloud Coding Challenge

The code is in clccc.py, and the tests are in
test_clccc.py

    $ python ./test_clccc.py # doesn't die

To see the data from the example:

    $ python ./test_clccc.py example
    Cloudy Coders, 2100
      Manager, Manager A, 300, 2100, 1
        Manager, Manager B, 300, 1800, 2
          Developer, Developer A, 1000, 1000, 0
          QA Tester, QA Tester A, 500, 500, 0

To see a deeper example that I made up (it also exposed a bug):

    $ python ./test_clccc.py deeper
    Cloudy Coders, 6500
      Manager, Manager A, 1900, 6500, 1
        Manager, Manager B, 1900, 4600, 2
          Developer, Developer A, 1200, 1200, 0
          QA Tester, QA Tester A, 1500, 1500, 0
    Fluffy Typers, 25300
      Manager, Big Kahuna, 1900, 11500, 2
        Manager, NotQuiteAs Big, 1900, 6500, 1
          Manager, Manny McMan, 1900, 4600, 2
            QA Tester, QQQQQ AAAAA, 1500, 1500, 0
            Developer, Imouta Names, 1200, 1200, 0
        Manager, Biff Biffer, 1900, 3100, 1
          Developer, Devin Dev, 1200, 1200, 0
      Manager, Pointy Director, 1900, 13800, 2
        Manager, Mary Lamb, 1900, 7300, 4
          Developer, Type-y Typer, 1200, 1200, 0
          Developer, Tappy Tapper, 1200, 1200, 0
          QA Tester, Bam Bam, 1500, 1500, 0
          QA Tester, Pebbles, 1500, 1500, 0
        Manager, Leafy Blue, 1900, 4600, 2
          Developer, Sarah Desert, 1200, 1200, 0
          QA Tester, Shiny Window, 1500, 1500, 0

And if you have py.test:

    $ py.test
    ============================= test session starts ==============================
    platform darwin -- Python 2.7.10, pytest-2.8.2, py-1.4.30, pluggy-0.3.1
    rootdir: <...>/git/CL-CCC, inifile:
    collected 3 items

    test_clccc.py ...

    =========================== 3 passed in 0.01 seconds ===========================
