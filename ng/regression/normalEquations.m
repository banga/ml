function theta = normalEquations(x, y)
  theta = pinv(X' * X) * X' * y;
endfunction
