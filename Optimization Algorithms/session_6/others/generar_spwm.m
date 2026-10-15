clear; clc; close all;

% Método 'teórico' usado por múltiples inversores, en el que, 
% los pulsos son proporcionales al valor de la función que 
% deseo aproximar en un momento dado. 

% Como deseo aproximar una función seno, en los extremos del semiciclo, 
% los pulsos son angostos, y en el centro, anchos

triang = 1.2 .* bartlett(40)';
x = [];
for k = 1:25
x = [x triang];
end
s = sin(pi.*(0:999)./1000);
vector = zeros(1,1000);
vector(s > x) = 1;