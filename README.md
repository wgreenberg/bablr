Bablr
=====

Borges' [Library of Babel](http://en.wikipedia.org/wiki/The_Library_of_Babel)
is to literature, as Bablr is to Twitter.

# Summary

Bablr is an implemenation of the Library of Babel thought experiment. However,
instead of being an enumeration of all possible 410 page books in a 23
character alphabet, it is an enumeration of all possible tweets in this 32
character alphabet:

`abcdefghijklmnopqrstuvwxyz  ,.@#`

This is neat because at some point, Bablr will produce a tweet which accurately
describes your favorite dessert. Or how your hair looks **right now**. Or the
exact circumstances of your birth.

Of course, this also means it'll produce millions of tweets with inaccurate
depictions of all of those things, and unfathomably many tweets that are
absolute gibberish.

# Technically incorrect

The tweets are generated via a function, `lookup`, that maps arbitrary strings
to tweets. This is done by interpreting the SHA512 digest of user input as a
bitstring of 5-bit characters (which yields our 32 character alphabet). Note
that this actually only produces 102 characters instead of the standard 140,
but who's counting anyway?

SHA512 is [expected but not proven](http://stackoverflow.com/a/2659174/4212349)
to be surjective on the set of 512 bit numbers, and hence Bablr is expected to
be capable of enumerating all possible tweets.
