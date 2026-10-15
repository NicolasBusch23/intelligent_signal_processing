% implementación del TSP (problema del vendedor viajero):
% clear ; close all; clc; 

% Tamaño del problema
N = 20;

% creación aleatoria del problema:
coordenadas = round(rand(N,2) .* 150);

eje = subplot(1,1,1);
xlabel('x_{ [km]}');
ylabel('y_{ [km]}');
set(eje,'FontSize',16);
axis([-2 152 -2 152]);
title('Problema del vendedor viajero');
grid minor;
for k=1:N
    texto = text(coordenadas(k,1),coordenadas(k,2),sprintf('%c','A'+k-1));
    set(texto,'FontSize',14,'HorizontalAlignment','center',...
        'FontWeight','bold');
end

% Crear nombres para las ciudades: A, B, C, ...
ciudades = arrayfun(@(k) char('A' + k - 1), 1:N, 'UniformOutput', false)';

% Crear y exportar tabla
T = table(ciudades, coordenadas(:,1), coordenadas(:,2), ...
    'VariableNames', {'ciudad', 'x_km', 'y_km'});

writetable(T, 'problem.csv');