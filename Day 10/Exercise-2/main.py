def summa(fname,lname):
  sum_fname = fname[0].upper();
  sum_lname = lname[0].upper();
  return sum_fname + fname[1:] + ' ' + sum_lname + lname[1:]


print(summa("su", "mu"))