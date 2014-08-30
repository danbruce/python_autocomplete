#!/usr/bin/python
#
# Copyright 2014 Daniel Bruce
from sys import argv, stdin, exit

class AutoComplete :
  """ A helpful class for retrieving the words matching a specified prefix"""
  def __init__(self, words, needsSort = False, containsDuplicates = False) :    
    if needsSort :
      words.sort()
    if containsDuplicates :
      self.words = self._removeDuplicates(words)
    else :
      self.words = words

  def findSuggestions(self, prefix) :
    """ Returns an array of words that match the given prefix """
    prefixLength = len(prefix)
    # perform a binary search for at least one word that matches the prefix
    index = self._findIndexUsingBinarySearch(
      prefix, prefixLength, 0, len(self.words)
    )
    # the helper method returns -1 when no word is given that matches the prefix
    if index == -1 :
      return [] # return an empty list in this case

    # scan towards the start of the list (starting from the found index) until
    # we no longer find a matching word
    first = index
    while first > 0 and self.words[first-1][:prefixLength] == prefix :
      first -= 1

    # scan towards the end of the list (starting from the found index) until we
    # no longer find a matching word
    last = index
    while last < len(self.words)-1 and self.words[last+1][:prefixLength] == prefix :
      last += 1
      
    # return the final list of words with duplicates removed
    return self.words[first:last+1]

  def _findIndexUsingBinarySearch(self, prefix, prefixLength, start, end) :
    """Performs a binary search to find the first word matching the given
    prefix
    """
    if start >= end :
      return -1 # we could not find any word matching that prefix
    # compute the middle index between start and end
    middle = int((end-start)/2) + start
    # and get the prefix for the word at that index
    checkWordPrefix = self.words[middle][:prefixLength]
    if prefix < checkWordPrefix :
      # search towards the start of the list recursively
      return self._findIndexUsingBinarySearch(
        prefix, prefixLength, start, middle
      )
    elif prefix > checkWordPrefix :
      # search towards the end of the list recursively
      return self._findIndexUsingBinarySearch(
        prefix, prefixLength, middle+1, end
      )
    else :
      # we found a matching word so return the index
      return middle

  def _removeDuplicates(self, aList) :
    """Removes duplicates from the original list under the assumption that the
    original list is sorted.
    """
    newList = []
    for item in aList :
      if not newList :
        newList.append(item)
      elif newList[-1] != item :
          newList.append(item)
    return newList

if __name__ == "__main__":
  try :
    if len(argv) < 2 :
      raise IOError('No data file specified.')
    dataFile = open(argv[1], 'r')
    autoComplete = AutoComplete(
      dataFile.read().splitlines(), needsSort=True, containsDuplicates=True
    )
  except IOError :
    print("Missing input file.")
    exit(1)

  while True :
    prefix = ""
    while not prefix :
      print("Please type the prefix of a word: ")
      prefix = stdin.readline().strip()
    matchingWords = autoComplete.findSuggestions(prefix)
    if not matchingWords :
      print("No matching words were found.")
    else :
      print("Suggestions:")
      print("\n".join(matchingWords))
