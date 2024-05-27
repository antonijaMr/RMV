%zadatak 1

% Definiranje DH parametara za antropomorfnu ruku (npr. 3DOF)
L1 = Link('d', 0, 'a', 1, 'alpha', 0);  % Prvi zglob
L2 = Link('d', 0, 'a', 1, 'alpha', 0);    % Drugi zglob
L3 = Link('d', 0, 'a', 1, 'alpha', 0);    % Treći zglob

% Kreirajte model robota
robot = SerialLink([L1 L2 L3], 'name', 'Antropomorfna Ruka');

% Korak 2: Planiranje trajektorije
% Početna i krajnja konfiguracija
q0 = [0 0 0];           % Početna konfiguracija
qf = [pi/2 -pi/3 pi/2]; % Krajnja konfiguracija

% Vrijeme trajanja trajektorije
T = 3; % trajanje u sekundama
t = linspace(0, T, 100); % Vremenski vektor

% Generiraj trajektoriju korištenjem interpolacije
[q, qd, qdd] = jtraj(q0, qf, t);

% Korak 3: Skiciranje isplaniranih trajektorija
figure;
subplot(3, 1, 1);
plot(t, q(:, 1));
title('Trajektorija zgloba 1');
xlabel('Vrijeme [s]');
ylabel('Kut [rad]');

subplot(3, 1, 2);
plot(t, q(:, 2));
title('Trajektorija zgloba 2');
xlabel('Vrijeme [s]');
ylabel('Kut [rad]');

subplot(3, 1, 3);
plot(t, q(:, 3));
title('Trajektorija zgloba 3');
xlabel('Vrijeme [s]');
ylabel('Kut [rad]');

% Korak 4: Animacija kretanja manipulatora
figure;
robot.plot(q);