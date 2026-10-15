%
MAXIT = 150;
best = zeros(MAXIT);

% límites del espacio:
x_min = -5;
x_max = 5;
w1 = 0.01 * ((x_max -x_min)/20);
w2 = 0.01 * ((x_max -x_min)/20);

% tamaño del enjambre:
N = 20;

% Enjambre aleatorio inicial
P = rand(N,2) .* (x_max - x_min) + x_min;

% velocidades aleatorias iniciales:
v = (rand(N, 2) .* 2 - 1) .* ((x_max -x_min)/20); % Velocidades aleatorias 

x1 = x_min:1e-1:x_max;
x2 = x_min:1e-1:x_max;

[X1,X2] = meshgrid(x1,x2);

f = 20 + X1.^2 + X2.^2 - 10.*(cos(2*pi.*X1)+cos(2*pi.*X2));
eje = subplot(1,2,1);
surf(X1,X2,f);
set(eje,'FontSize',15);
xlabel('x_1');
ylabel('x_2');
zlabel('f(x_1,x_2)');

for k=1:N
    texto = text(P(k,1),P(k,2),rastrigin(P(k,1),P(k,2)),...
        'X','FontSize',60,'Color',[1 0 0],...
        'HorizontalAlignment','center',VerticalAlignment='top');
end
msgbox('Ajuste el punto de vista...','modal');
pause;
[az,el] = view;
P_iBest = P;

i = 1;
while(i<MAXIT)

    fit_iBest = rastrigin(P(:,1),P(:,2));
    fit_GBest = min(fit_iBest);
    P_GBest = P_iBest(fit_GBest == fit_iBest);
    P_GBest = P_GBest(1);
    P = P + v;
    best(i) = fit_GBest;

    % eje = subplot(2,1,1);
    eje = subplot(1,2,1);
    surf(X1,X2,f);
    set(eje,'FontSize',15);
    xlabel('x_1');
    ylabel('x_2');
    zlabel('f(x_1,x_2)');

    for k=1:N
        texto = text(P(k,1),P(k,2),rastrigin(P(k,1),P(k,2)),...
            'X','FontSize',60,'Color',[1 0 0],...
            'HorizontalAlignment','center',VerticalAlignment='top');
    end
    view(az,el);
    if(i>1)
        eje = subplot(1,2,2);
        plot(best(1:i),'LineWidth',2);
        grid minor;
        xlabel('Iterations');
        title('Fitness( P_{GBest} )');
    end
    pause(0.2);


    % Actualizar las velocidades
    v = v + w1 .* rand(N, 2) .* (P_iBest - P) + w2 .* rand(N, 2) .* (P_GBest - P);

    % Actualizar P_iBest
    for k= 1: N
        if fit_iBest(k) < rastrigin(P_iBest(k,1), P_iBest(k,2))
            P_iBest(k, :) = P(k, :);
        end 
    end
   
    % Asegurarse de que las partículas se mantengan dentro de los límites
    P = max(min(P, x_max), x_min);
    i = i + 1;
end





function [z] = rastrigin(x1,x2)
    z = 20 + x1.^2 + x2.^2 - 10.*(cos(2*pi.*x1) + cos(2*pi.*x2));
end