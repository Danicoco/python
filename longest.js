function longest(arg){
        var words = arg.replace(/[^A-Za-z0-9\s]/g, "").split(" ");
        var longestWord = words.reduce( function( longestSoFar, currentWord ) {
          return currentWord.length > longestSoFar.length ? currentWord : longestSoFar;
        },"");
        return longestWord;
    }

document.write(longest( 'This is Andela' ));
