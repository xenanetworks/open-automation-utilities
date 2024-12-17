Executable for Windows
===========================

Generate SSH Key
-----------------

AN/LT Utility requires an SSH key pair to run as a SSH service. To generate a SSH key pair, please open Command Prompt or PowerShell on Windows.


.. code-block:: doscon

    > ssh-keygen -t rsa

You will be prompted to save and name the key. **If not found**, read `Generate SSH Keys in Windows 10/11 <https://linuxhint.com/generate-ssh-keys-windows-11/>`_.

.. code-block:: doscon

    > Generating public/private rsa key pair. Enter file in which to save the key (C:\Users\USER\.ssh\id_rsa):

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

This will generate two files, by default called ``id_rsa`` and ``id_rsa.pub`` in ``C:\Users\USER\.ssh``

.. seealso::

    You can read more about `Generating SSH Key <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key>`_ 

.. attention::

    If your machine doesn't have internet access, you should generate the SSK keys on another machine and copy the keys to your target machine.

Download Windows Executable
-----------------------------------------

Download :download:`xoa-utils-win-x64-<version>.zip <https://github.com/xenanetworks/open-automation-utilities/releases>`. 

Start AN/LT Utility
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Unzip the file and run ``xoa-utils-win-x64-<version>.exe``. The executable includes Python itself, `xoa-driver <https://pypi.org/project/xoa-driver/>`_, and all the dependencies.

.. important::
    
    There is **no need to install Python or any Python packages** on your PC to run the AN/LT Utility Windows executable, but remember **you still need to generate the SSH key**.


.. code-block:: doscon

    > xoa-utils
    (PID: 12345) AN/LT Utility SSH Service (1.1.0) running on 0.0.0.0:22622.


.. note::

    Unlike the Python package, you can't change the port number on which you run the SSH server if using the Windows executable.