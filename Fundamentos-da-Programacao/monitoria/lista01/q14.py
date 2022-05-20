def anDeUmaPA(a1, r, n):
  return (a1+(n-1)*r);

a1 = int(input("a1: "));
r = int(input("r: "));
n = int(input("n: "));

an = anDeUmaPA(a1, r, n);
print(f"an: {an}");
# 1 3 5 7