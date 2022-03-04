# Coin Mixer

## Aim:

Accept the incoming address and list of addresses. Tumble the coins Accept coins from address and break the amount into
different parts and send it to addresses provided.

## Solution:

After transferring the funds to central wallet, we need to distribute amount to the provided wallet addresses.

1. We need to divide the amount in random ratios for the wallet, this will prevent backtracking.
2. Once we have decided how much we want to send to an address, we can further split that amount into smaller chunks
   and 'trickle' down the amount.
3. We need to do it in a way that number of transactions that we do shouldn't cost us too much transaction fees (this
   will be the last part)

Dividing an amount into ratios:
Lets say we use precision up to 5 decimal points for simplicity i.e. smallest Jobcoin transaction is 0.00001 we randomly
select a number between 0 - 1 exclusive, and subtract that. This becomes our first cut, from remaining we randomly cut
another piece, and we repeat till we have got random ratios for all the addresses.

After deciding the ratios we are going to break up the amount for the addresses, and for each address we need to create
a trickling transactions. For each address we separate them into multiple transactions and with random transaction
timestamp and perform the transactions. 
