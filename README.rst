=====================
Doppelganger
=====================

| Create a file with an alternative extension from an original file.
| This tool accomplishes the following in Zsh.

.. code-block:: sh

 $  for fn in *.txt; do cp $fn ${fn%.txt}.log; done

Usage
========

.. code-block:: sh

    $ poetry shell
    $ poetry install
    $ doppelganger log --ofe=txt

    You can see help with -h.

    $ doppelganger -h

Dependencies
========

| fire = ^0.3.1
| tqdm = ^4.48.2
