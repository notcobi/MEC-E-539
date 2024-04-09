sym h
eqn = sqrt(22.5*sqrt((1 + (h/0.8)^2))/(0.0245*h))*pi/sqrt((0.8)^2 + h^2) == 94.25;
sol = vpasolve(eqn, h)