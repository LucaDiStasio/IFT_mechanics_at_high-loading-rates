%%
%==============================================================================
% Copyright (c) 2016 Université de Lorraine & Luleå tekniska universitet
% Author: Luca Di Stasio <luca.distasio@gmail.com>
%                        <luca.distasio@ingpec.eu>
%
% Redistribution and use in source and binary forms, with or without
% modification, are permitted provided that the following conditions are met:
% 
% 
% Redistributions of source code must retain the above copyright
% notice, this list of conditions and the following disclaimer.
% Redistributions in binary form must reproduce the above copyright
% notice, this list of conditions and the following disclaimer in
% the documentation and/or other materials provided with the distribution
% Neither the name of the Université de Lorraine or Luleå tekniska universitet
% nor the names of its contributors may be used to endorse or promote products
% derived from this software without specific prior written permission.
% 
% THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
% AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
% IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
% ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
% LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
% CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
% SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
% INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
% CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
% ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
% POSSIBILITY OF SUCH DAMAGE.
%==============================================================================
%
%  DESCRIPTION
%  
%  A script to interface the mesh generation algorithms in matlab to the
%  Mathematica GUI
%
%%

clear all
close all
clc

%-------------------------------------------------------------------------%
%-------------------------------------------------------------------------%
%-                          Input Data                                   -%
%-------------------------------------------------------------------------%
%-------------------------------------------------------------------------%

                                                                           % flags for model type
IFTtest = 1;                                                               % 1 -> Double Cantilever Beam (DCB)
                                                                           % 2 -> End Notched Flexure (ENF)
                                                                           % 3 -> Mixed Mode Bending (MMB)

x0 = 0;
y0 = 0;
z0 = 0;

lx = [1;2;3;1];
ly = [10;10;20;30;5;5;2];
lz = [2.5;7.5];

Nx = [10;15;12;5];
Ny = [20;5;2;50;20;15;7];
Nz = [20;10];

element = 2;                                                               % Element type: 1 --> quads, 2 --> tri
order = 1;

optimize = true;                                                          % Perform optimization of mesh

%-------------------------------------------------------------------------%
%-------------------------------------------------------------------------%
%-                        Mesh Generation                                -%
%-------------------------------------------------------------------------%
%-------------------------------------------------------------------------%

%[nodes] = gradedHexahedron(x0,y0,z0,lx,ly,lz,Nx,Ny,Nz);
[nodes] = gradedRectangle(x0,y0,lx,ly,Nx,Ny);

%-------------------------------------------------------------------------%
%-------------------------------------------------------------------------%
%-                         Visualization                                 -%
%-------------------------------------------------------------------------%
%-------------------------------------------------------------------------%

% fig0 = figure();
% plot3(nodes(:,1),nodes(:,2),nodes(:,3),'b.')
% hold on
% grid on
% xlabel('x')
% ylabel('y')
% zlabel('z')
% title('IFT mesh')
% axis equal
% l = max([sum(lx);sum(ly);sum(lz)]);
% axis([-1.1*l 1.1*l -1.1*l 1.1*l -1.1*l 1.1*l])
% % hold on
% % for i=1:size(nodes,1)
% %     plot(nodes(i,1),nodes(i,2),'b.')
% %     hold on
% %     pause(0.01)
% % end

fig0 = figure();
plot(nodes(:,1),nodes(:,2),'b.')
hold on
grid on
xlabel('x')
ylabel('y')
title('IFT mesh')
axis equal
l = max([sum(lx);sum(ly)]);
axis([-1.1*l 1.1*l -1.1*l 1.1*l])
% hold on
% for i=1:size(nodes,1)
%     plot(nodes(i,1),nodes(i,2),'b.')
%     hold on
%     pause(0.01)
% end