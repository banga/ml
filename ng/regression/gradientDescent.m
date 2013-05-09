function [theta, cost_history] = gradientDescent(x, y, alpha, num_iters)
  [n, m] = size(x);
  theta = zeros(n, 1);
  cost_history = zeros(num_iters, 1);

  for i = 1:num_iters
    err = theta' * x - y;
    delta = (1 / m) * x * err';
    theta = theta - alpha * delta;
    cost_history(i) = costFunction(theta, x, y);
  endfor
endfunction
