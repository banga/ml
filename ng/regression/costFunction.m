function J = costFunction(theta, x, y)
  m = size(x, 2);
  err = theta' * x - y;
  J = (1 / 2*m) * (err * err');
endfunction
