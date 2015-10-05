__author__ = 'sridhar'

def longestWords( dictionary):
        # write your code here
        results ={}
        for key in dictionary:
            print key
            print results
            if len(key) in results:
                results[len(key)]=results.get(len(key))+[key]
            else:
                results[len(key)]=[key]

        print results.get(max(results.keys()))


longestWords({
  "dog",
  "google",
  "facebook",
  "internationalization",
  "blabla"
})