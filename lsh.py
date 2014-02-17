#!/usr/bin/env python
import numpy as np
import itertools as it

class lsh():
  def __init__(self, vecsize, mu=5.0, sig=1.0, r=5.0, buckets=10):
    self.a = [np.random.normal(mu, sig, vecsize) for _ in xrange(vecsize)]
    self.b = [np.random.uniform(0, r) for _ in xrange(vecsize)]
    self.h = [dict() for _ in xrange(vecsize)]
    self.r = r
    return

  def lshash(self, vec, avec, bval):
    return int(np.floor(vec.dot(avec) + bval / self.r))

  def __setitem__(self, vec, value):
    for idx, (a, b) in enumerate(it.izip(self.a, self.b)):
      hashval = self.lshash(vec, a, b)
      hashable_vec = tuple(vec)
      self.h[idx].setdefault(hashval, dict())[hashable_vec] = value

  def __getitem__(self, vec):
    avec = self.a[0]
    bval = self.b[0]
    hashval = self.lshash(vec, avec, bval)
    hashable_vec = tuple(vec)
    return self.h[0][hashval][hashable_vec]

  def nearest(self, vec):
    all_results = dict()
    for idx, (a, b) in enumerate(it.izip(self.a, self.b)):
      hashval = self.lshash(vec, a, b)
      hashable_vec = tuple(vec)
      bucket = self.h[idx].get(hashval, dict())
      all_results.update(bucket)
    return all_results

def main():
  pass

if __name__ == "__main__":
  main()
