# Normalize the data around the mean and one standard deviation
function [xn, mu, sigma] = normalize(x)
  m = size(x, 2);
  mu = mean(x, 2);
  sigma = std(x, 0, 2);
  xn = (x - repmat(mu, 1, m)) ./ repmat(sigma, 1, m);
endfunction
