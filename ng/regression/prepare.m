# Prepare the training samples for gradient descent
function [x, mu, sigma] = prepare(x)
  m = size(x, 2);
  [x, mu, sigma] = normalize(x);
  x = [ones(1, m); x];
endfunction

