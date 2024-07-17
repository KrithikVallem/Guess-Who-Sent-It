# Guess Who Sent It!
A game where you guess who in the groupchat sent a particular reel/quote/image!

## Steps to run
- Make a spreadsheet where 1st column is names and 2nd column is links/quotes
- Download as a tsv file (not csv) because many quotes include commas
    - Verify that tabs aren't breaking anything either
- Put the tsv file in this repo's `data` folder and rename it `data.tsv`
- Run `tsvToJs.py` from within the `data` folder to output a `data.js` file for the website to use
    - Change certain variables at the top depending on the format of your data
- Open `index.html` in your browser and enjoy!