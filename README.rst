=====================
Doppelganger
=====================

Create a file with an alternative extension from an original file.
This tool accomplishes the following in Zsh.

.. code-block:: sh

 $  for fn in *.txt; do cp $fn ${fn%.txt}.log; done

Usage
========

.. code-block:: sh

    $ poetry shell
    $ poetry install
    $ doppelganger alternative_file_extension

Dependencies
========

    fire = ^0.3.1
    tqdm = ^4.48.2
