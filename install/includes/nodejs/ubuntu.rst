.. code-block:: sh

   # see https://github.com/nodesource/distributions#debian-and-ubuntu-based-distributions 
   # for detailed installation instructions.

   $ apt install -y ca-certificates curl gnupg
   $ mkdir -p /etc/apt/keyrings
   $ curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg
   $ NODE_MAJOR=20
     echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | sudo tee /etc/apt/sources.list.d/nodesource.list
   $ apt update
   $ apt install nodejs -y