clear
clc
%% Define simulation parameters
N = 100;          % 100 CVs
L = 1.0;          % [m] Length of the rod
dx = L/N;         % [m] Distance between the nodal points [Don't change]
Pe_1 = 0.1;       % Peclet number 1
Pe_2 = 100;       % Peclet number 2
T_A = 0;          % [C] Temperature at the left boundary
T_B = 1;          % [C] Temperature at the right boundary

%% Define variable size [Don't change]
aW_1 = zeros(N,1);
aE_1 = zeros(N,1);
aP_1 = zeros(N,1);
qP_1 = zeros(N,1);
qu_1 = zeros(N,1);
AA_1 = zeros(N,1);
CD_1 = zeros(N,1);

aW_2 = zeros(N,1);
aE_2 = zeros(N,1);
aP_2 = zeros(N,1);
qP_2 = zeros(N,1);
qu_2 = zeros(N,1);
AA_2 = zeros(N,1);
CD_2 = zeros(N,1);

%% Calculate coefficients of the discretized equations for internal nodes ------------
T_1 = convection_diffusion_1D(N,Pe_1,dx, T_A, T_B);
T_2 = convection_diffusion_1D(N,Pe_2,dx, T_A, T_B);

%% Analytical solution ------
x = dx/2:dx:(L-dx/2);
T_hat_anal_1 = (exp(Pe_1*x) - 1)/(exp(Pe_1) - 1);
T_hat_anal_2 = (exp(Pe_2*x) - 1)/(exp(Pe_2) - 1);

%% Error calculation
error_1 = abs(T_hat_anal_1 - T_1);
error_2 = abs(T_hat_anal_2 - T_2);

[T_1_max_error, T_1_max_error_index] = max(error_1);
[T_2_max_error, T_2_max_error_index] = max(error_2);

%% Plot the results
% Peclet number 1
figure(1)
y=dx/2:dx:(L-dx/2);
plot(x,T_hat_anal_1, 'k-', y, T_1, 'ks--', 'MarkerSize',2)
xlabel('Distance \itx, [m]')
ylabel('Temperature \itT, [C]')
title('Peclet number 0.1')
legend('Exact solution','Numerical solution')
saveas(gcf,'peclet_0.1.png')

% Peclet number 2
figure(2)
plot(x,T_hat_anal_2, 'k-', y, T_2, 'ks--', 'MarkerSize',2)
xlabel('Distance \itx, [m]')
ylabel('Temperature \itT, [C]')
title('Peclet number 100')
legend('Exact solution','Numerical solution')
saveas(gcf,'peclet_100.png')

% Error for Peclet number 1
figure(3)
hold on
plot(x, error_1, 'ks--', 'MarkerSize',2)
plot(x(T_1_max_error_index), T_1_max_error, 'ro', 'MarkerSize',5)
xlabel('Distance \itx, [m]')
ylabel('Absolute Error')
title('Absolute Error for Peclet number 0.1')
legend('Error','Max error', 'Location', 'best')
saveas(gcf,'error_0.1.png')

% Error for Peclet number 2
figure(4)
hold on
plot(x, error_2, 'ks--', 'MarkerSize',2)
plot(x(T_2_max_error_index), T_2_max_error, 'ro', 'MarkerSize',5)
xlabel('Distance \itx, [m]')
ylabel('Absolute Error')
title('Absolute Error for Peclet number 100')
legend('Error','Max error', 'Location', 'best')
saveas(gcf,'error_100.png')


%% Function to solve the 1D convection-diffusion equation
function [T] = convection_diffusion_1D(N,Pe,dx, T_A, T_B)
    %% Calculate coefficients of the discretized equations for internal nodes ------------
    for i=2:(N-1)
        aE(i) = 1/(Pe*dx);
        aW(i) = 1/(Pe*dx) + 1;
        aP(i) = 2/(Pe*dx) + 1;
    end
    %% Calculate coefficients for the boundary volumes --------------------------------
    % West (A point)
    aE(1) = 1/(Pe*dx) - 1;
    aW(1) = 0;
    qP(1) = 0;
    qu(1) = 2/(Pe*dx) * T_A;
    aP(1) = 3/(Pe*dx) - 1;
    % East (B point)
    aE(N) = 0;
    aW(N) = -1/(Pe*dx) - 1;
    qP(N) = 0;
    qu(N) = -2/(Pe*dx) * T_B;
    aP(N) = -3/(Pe*dx) - 1;

    %% Solution of the system of algebraic equations
    %  TDMA procedure
    AA(1)=aE(1)/aP(1);
    CD(1)=qu(1)/aP(1);
    for i=2:N
        AA(i)=aE(i)/(aP(i)-aW(i)*AA(i-1));
        CD(i)=(aW(i)*CD(i-1)+qu(i))/(aP(i)-aW(i)*AA(i-1));
    end
    %
    T(N)=CD(N);
    for i=N-1:-1:1
        T(i)=AA(i)*T(i+1)+CD(i);
    end
end