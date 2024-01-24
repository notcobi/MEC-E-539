syms u(x, y) w(x, y)

% Define the velocity vector
v = [u; w];

% Compute the gradient of v
grad_v = jacobian(v, [x, y]);

% Compute the divergence of the gradient of v
div_grad_v = divergence(grad_v, [x, y]);

% Display the result
disp('Divergence of the gradient of v:')
disp(div_grad_v)
