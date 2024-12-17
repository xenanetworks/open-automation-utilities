Python Package for macOS/Linux/Windows
======================================


Generate SSH Key
-----------------

AN/LT Utility requires an SSH key pair to run as a SSH service. To generate a SSH key pair, please open Command Prompt/PowerShell (Windows) or Terminal (macOS/Linux)

.. code-block:: doscon

    > ssh-keygen -t rsa

You will be prompted to save and name the key.

.. code-block:: doscon

    > Generating public/private rsa key pair. Enter file in which to save the key (/Users/USER/.ssh/id_rsa):

Press :kbd:`Enter` to use the default name ``id_rsa``. 

.. important::
    
    The filename of the key should be ``id_rsa``. Please don't use other filenames otherwise the application won't be able to run. 

Next you will be asked to create and confirm a passphrase for the key:

.. code-block:: doscon

    > Enter passphrase (empty for no passphrase):

Press :kbd:`Enter` to skip passphrase.

.. code-block:: doscon

    > Enter same passphrase again:

Press :kbd:`Enter` again to confirm passphrase.

This will generate two files, by default called ``id_rsa`` and ``id_rsa.pub`` in ``/Users/USER/.ssh``


.. seealso::

    You can read more about `Generating SSH Key <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key>`_ 


Python Package for Win/macOS/Linux
---------------------------------------------

.. note::

    Skip this section, if you are a Windows (x64) user and don't want to install AN/LT Utility as a Python package but simply want the **.exe** application,


AN/LT Utility is available to install via the `Python Package Index <https://pypi.org/>`_. You can also install from the source file. The steps below will guide you through 

Prerequisites
^^^^^^^^^^^^^

Before installing AN/LT Utility, please make sure your environment has installed:
    
* `Install Python`_ (requires **Python >= 3.8**)
* `Install PIP`_

Install Python
""""""""""""""

.. important:: 

    AN/LT Utility requires Python >= 3.8.


AN/LT Utility requires that you `download and install Python3 <https://www.python.org/downloads/>`_ on your system.

.. note::

    If you use **Windows**, remember to check **Add python.exe to PATH**.

    .. figure:: ../../_static/python_installation.png
        :width: 100 %
        :align: center

After installation, open **Command Prompt** (Windows) or **Terminal** (macOS/Linux) and type ``python`` to verify your Python installation.

.. tab:: Windows

    .. code-block:: doscon
        :caption: Check Python installation in Windows.

        > python
        Python 3.10.10 (tags/v3.10.10:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
        Type "help", "copyright", "credits" or "license" for more information.
        >>>

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: Check Python installation in macOS/Linux.

        $ python3
        Python 3.10.10 (v3.10.10:a58ebcc701, Feb 7 2023, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
        Type "help", "copyright", "credits" or "license" for more information.
        >>> 

.. note::

    🧐 If you are stuck with Python installation, seek help in `Python 3 Installation & Setup Guide <https://realpython.com/installing-python/>`_


Install PIP
"""""""""""

Make sure ``pip`` is installed on your system. ``pip`` is the `package installer for Python <https://packaging.python.org/guides/tool-recommendations/>`_ . You can use it to install packages from the `Python Package Index <https://pypi.org/>`_  and other indexes.

Usually, ``pip`` is automatically installed if you are:

* working in a `virtual Python environment <https://packaging.python.org/en/latest/tutorials/installing-packages/#creating-and-using-virtual-environments>`_ (`virtualenv <https://virtualenv.pypa.io/en/latest/#>`_ or `venv <https://docs.python.org/3/library/venv.html>`_ ). It is not necessary to use ``sudo pip`` inside a virtual Python environment.
* using Python downloaded from `python.org <https://www.python.org/>`_ 

If you don't have ``pip`` installed, you can:

* Download the script, from https://bootstrap.pypa.io/get-pip.py.
* Open a terminal/command prompt, ``cd`` to the folder containing the ``get-pip.py`` file and run:

.. tab:: Windows

    .. code-block:: doscon
        :caption: Install pip in Windows environment.

        > py get-pip.py

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: Install pip in macOS/Linux environment.

        $ python3 get-pip.py

.. seealso::

    Read more details about this script in `pypa/get-pip <https://github.com/pypa/get-pip>`_.

    Read more about installation of ``pip`` in `pip installation <https://pip.pypa.io/en/stable/installation/>`_.


Install From PyPi Repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``pip`` is the recommended installer for AN/LT Utility. The most common usage of ``pip`` is to install from the `Python Package Index <https://pypi.org/>`_ using `Requirement Specifiers <https://pip.pypa.io/en/stable/cli/pip_install/#requirement-specifiers>`_.

.. note::
    
    If you install AN/LT Utility using ``pip install xoa-utils``, XOA Python API (PyPI package name `xoa_driver <https://pypi.org/project/xoa-python-api/>`_) will be automatically installed.

.. important::

    You can **either** install xoa-utils in your global Python namespace/package inventory **or** you can create a virtual Python environment to prevent polluting your global Python package inventory

.. _install_core_global:

If Install To Global Namespace
"""""""""""""""""""""""""""""""

.. tab:: Windows
    :new-set:

    .. code-block:: doscon
        :caption: Install AN/LT Utility in Windows environment from PyPI.

        > pip install xoa-utils            # latest version
        > pip install xoa-utils==1.0.0     # specific version
        > pip install xoa-utils>=1.0.0     # minimum version

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: Install AN/LT Utility in macOS/Linux environment from PyPI.

        $ pip install xoa-utils            # latest version
        $ pip install xoa-utils==1.0.0     # specific version
        $ pip install xoa-utils>=1.0.0     # minimum version


.. _install_core_venv:

If Install To Virtual Environment
""""""""""""""""""""""""""""""""""

Install AN/LT Utility in a virtual environment, so it does not pollute your global namespace. 

For example, your project folder is called ``/my_xoa_project``.

.. tab:: Windows

    .. code-block:: doscon
        :caption: Install AN/LT Utility in a virtual environment in Windows from PyPI.

        [my_xoa_project]> python -m venv .\env
        [my_xoa_project]> .env\Scripts\activate

        (env) [my_xoa_project]> pip install xoa-utils         # latest version
        (env) [my_xoa_project]> pip install xoa-utils==1.0.0  # specific version
        (env) [my_xoa_project]> pip install xoa-utils>=1.0.0  # minimum version

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: Install AN/LT Utility in a virtual environment in macOS/Linux from PyPI.

        [my_xoa_project]$ python3 -m venv ./env
        [my_xoa_project]$ source ./env/bin/activate

        (env) [my_xoa_project]$ pip install xoa-utils         # latest version
        (env) [my_xoa_project]$ pip install xoa-utils==1.0.0  # specific version
        (env) [my_xoa_project]$ pip install xoa-utile>=1.0.0 # minimum version

Afterwards, your project folder will be:

.. code-block::
    :caption: After creating Python virtual environment

    /my_xoa_project
        |
        |- env

.. seealso::

    * `Virtual Python environment <https://packaging.python.org/en/latest/tutorials/installing-packages/#creating-and-using-virtual-environments>`_
    * `virtualenv <https://virtualenv.pypa.io/en/latest/#>`_
    * `venv <https://docs.python.org/3/library/venv.html>`_


Upgrade From PyPi Repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To upgrade AN/LT Utility package from PyPI:

.. tab:: Windows
    :new-set:
    
    .. code-block:: doscon
        :caption: Upgrade AN/LT Utility in Windows environment from PyPI.

        > pip install xoa-utils --upgrade

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: Upgrade AN/LT Utility in macOS/Linux environment from PyPI.

        $ pip install xoa-utils --upgrade


.. note::
    
    If you upgrade AN/LT Utility using ``pip install --upgrade xoa-utils``, XOA Python API (PyPI package name `xoa_driver <https://pypi.org/project/xoa-python-api/>`_) will be automatically upgraded.


Install Manually From Source
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you don't have internet access, you can install AN/LT Utility manually from source, the steps are:

**Step 1**, make sure Python packages `wheel <https://wheel.readthedocs.io/en/stable/>`_ and  `setuptools <https://setuptools.pypa.io/en/latest/index.html>`_ are installed on your system. Install ``wheel`` and ``setuptools`` using ``pip``:

.. tab:: Windows
    :new-set:

    .. code-block:: doscon
        :caption: Install ``wheel`` and ``setuptools`` in Windows environment.

        > pip install wheel setuptools

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: Install ``wheel`` and ``setuptools`` in macOS/Linux environment.

        $ pip install wheel setuptools

**Step 2**, download the AN/LT Utility source distribution from `AN/LT Utility Releases <https://github.com/xenanetworks/open-automation-core/releases>`_. Unzip the archive and run the ``setup.py`` script to install the package:

.. tab:: Windows
    :new-set:

    .. code-block:: doscon
        :caption: Install AN/LT Utility in Windows environment from source.

        [xoa_core]> python setup.py install

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: Install AN/LT Utility in macOS/Linux environment from source.

        [xoa_core]$ python3 setup.py install


**Step 3**, if you want to distribute, you can build ``.whl`` file for distribution from the source:

.. tab:: Windows
    :new-set:

    .. code-block:: doscon
        :caption: Build AN/LT Utility wheel in Windows environment for distribution.

        [xoa_core]> python setup.py bdist_wheel

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: Build AN/LT Utility wheel in macOS/Linux environment for distribution.

        [xoa_core]$ python3 setup.py bdist_wheel

.. important::

    If you install AN/LT Utility from the source code, you need to install XOA Python API (PyPI package name `xoa_driver <https://pypi.org/project/xoa-python-api/>`_) separately. This is because XOA Python API is treated as a 3rd-party dependency of AN/LT Utility. You can go to `XOA Python API <https://github.com/xenanetworks/open-automation-python-api>`_ repository to learn how to install it.


Start AN/LT Utility
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After installing the package and ensuring the SSH key in place, you can start AN/LT Utility simply by typing ``xoa-utils``

.. tab:: Windows
    :new-set:

    .. code-block:: doscon
        :caption: Start AN/LT Utility SSH service.

        > xoa-utils
        (PID: 12345) AN/LT Utility SSH Service (1.1.0) running on 0.0.0.0:22622.


.. tab:: macOS/Linux

    .. code-block:: console
        :caption: Start AN/LT Utility SSH service.

        $ xoa-utils
        (PID: 12345) AN/LT Utility SSH Service (1.1.0) running on 0.0.0.0:22622.

.. note::

    If you want to run xoa-utils SSH service on a different port, do ``xoa-utils <port number>``



Uninstall and Remove Unused Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``pip uninstall xoa-utils`` can uninstall the package itself but not its dependencies. Leaving the package's dependencies in your environment can later create conflicting dependencies problem.

We recommend install and use the `pip-autoremove <https://github.com/invl/pip-autoremove>`_ utility to remove a package plus unused dependencies.

.. tab:: Windows
    :new-set:

    .. code-block:: doscon
        :caption: Uninstall AN/LT Utility in Windows environment.

        > pip install pip-autoremove
        > pip-autoremove xoa-utils -y

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: Uninstall AN/LT Utility in macOS/Linux environment.

        $ pip install pip-autoremove
        $ pip-autoremove xoa-utils -y

.. seealso::

    See the `pip uninstall <https://pip.pypa.io/en/stable/cli/pip_uninstall/#pip-uninstall>`_ reference.

    See `pip-autoremove <https://github.com/invl/pip-autoremove>`_ usage.