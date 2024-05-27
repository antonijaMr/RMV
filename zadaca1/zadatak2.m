% Definisanje početne i krajnje transformacije
Ti = [1 0 0 0.6;
      0 1 0 -0.5;
      0 0 1 0;
      0 0 0 1];
  
Tf = [1 0 0 0.4;
      0 1 0 0.5;
      0 0 1 0.2;
      0 0 0 1];

% Učitavanje modela Puma560 iz Robotics Toolbox-a
mdl_puma560;

% Rješavanje inverzne kinematike za početnu tačku
q_initial = p560.ikine(Ti);

% Rješavanje inverzne kinematike za krajnju tačku
q_final = p560.ikine(Tf);

% Definisanje vremena trajanja i broja tačaka na putanji
t = linspace(0, 2, 100);

% Interpolacija između početne i krajnje tačke
q_traj = jtraj(q_initial, q_final, t);

% Kreiranje figure za animaciju
figure;
p560.plot(q_traj);