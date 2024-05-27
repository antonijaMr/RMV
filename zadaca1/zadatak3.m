% zadatak 3
% ucitavanje modela puma 560
mdl_puma560;

% definisanje inicijalne konfiguracije
qz=[0 0 0 0 0 0];

%compute gravity toruques at qz
tau = p560.gravload(qz);

%Time vector
t = linspace(0,10,100); %10 seconds, 100 points

%Define the joint trajectories(here we assume the robot stays at qz)
q = repmat(qz, length(t), 1);

%plot joint trajectories
figure;
plot(t,q);
xlabel('Time [s]');
ylabel('Joint angles [rad]');
title('Joint trajectories');
legend('q1','q2','q3','q4','q5','q6');
grid on;

%animate the robot
figure;
p560.plot(q);
q