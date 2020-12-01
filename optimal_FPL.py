# Use Gurobi Integer Program to find the optimal FPL team.
import pandas as pd
from gurobipy import *
import numpy as np
import scipy

#data_frame = pd.read_csv("FPLPlayerData.txt",
# sep = "\t")
#data_frame = pd.read_csv("FPLPlayerData2.csv")
data_frame = pd.read_csv("~/fantasy-RL/player_initial_values_1819_FINAL.csv")
#minutes = data_frame['minutes']
#data_frame = data_frame[minutes > 900]
num_players = len(data_frame)
print("num_players = ", num_players)
#print(data_frame.head())

###### 18/19 Data Read in ####################
cost = data_frame['cost']
player = data_frame['full_names'] 
selected_by = data_frame['selected']
team = data_frame['team']
#player = data_frame['web_name']

#utilization = data_frame['selected_by_percent']
#team = data_frame['team']
#club = data_frame['club']
#position = data_frame['position']
#value = data_frame['value_season']
#points = data_frame['total_points']
#minutes = data_frame['minutes']
#ict = data_frame['ict_index_rank']
#cop = data_frame['chance_of_playing_next_round']
#elite_selected = data_frame['elite_selected']
#elite_selected = elite_selected.fillna(0)

#ppm = points/minutes

#ppm_played = ppm[minutes > 90]
#num_players = len(ppm_played)
#vectorize these from Series
#utilization = utilization.values
selected_by = selected_by.values
cost = cost.values
#value = value.values
#points = points.values
#ppm = ppm.values
#ict = ict.values
#elite_selected = elite_selected.values
#create numpy array for position matrix
#positions = ['GK', 'D', 'M', 'F']
GK_vec = data_frame.element_type == 1
D_vec = data_frame.element_type == 2
M_vec = data_frame.element_type == 3
F_vec = data_frame.element_type == 4
#print(GK_vec.head())
#print(D_vec.head())

pos_matrix = np.append([GK_vec],[D_vec, M_vec, F_vec], 
	axis = 0).astype(int)
#print(pos_matrix[0:4, :])
#print(pos_matrix.shape)

#use this to optimize XIs/15s
pos_constrs = np.array([2, 5, 5, 3])


#create numpy array for team constraints
#unique_teams = np.unique(data_frame.Team)
unique_teams = np.arange(20)
unique_teams += 1
#print(unique_teams)


#teams can't have more than 3 players
team_constrs = np.repeat(3,20)

#matrix of 1s and 0s for a player's team 
team_matrix = np.zeros([20,num_players]) 


for i in range(len(unique_teams)):
	team_matrix[i, :] = data_frame.team == unique_teams[i]

team_matrix = team_matrix.astype(int)


#create model
m = Model(name="ip")

#add num_players binary array variables 
use = m.addMVar(num_players, vtype=GRB.BINARY, name = "use")
#use = m.addMVar(len(ppm_played), vtype=GRB.BINARY, name = "use")
#add objective
# @ is matrix multiplication
# here we maximize the inner product of utilization and use
# can pick any quantity to maximize (ICT score, points last season) 

m.setObjective(selected_by @ use, GRB.MAXIMIZE)
#m.setObjective(utilization @ use, GRB.MAXIMIZE)
#m.setObjective(elite_selected @ use, GRB.MAXIMIZE)
#m.setObjective(value @ use, GRB.MAXIMIZE)
#m.setObjective(points @ use, GRB.MAXIMIZE)
#m.setObjective(ppm_played @ use, GRB.MAXIMIZE)
#m.setObjective(ppm @ use, GRB.MAXIMIZE)
#m.setObjective(ict @ use, GRB.MINIMIZE)
#add team constraint
# Constraints in the form of Ax=b
m.addMConstrs(A=team_matrix, x=use, sense='<=', b=team_constrs)

#add position constraint
m.addMConstrs(A=pos_matrix, x=use, sense='=', 
	b=pos_constrs)

#add cost constraint
m.addConstr(cost @ use <= 1000)

m.optimize()

var = m.getVars()

variables = []

for i in range(len(var)):
	
	variables.append(var[i].x)
	if abs(var[i].x - 1) <= 1e-10:
		print(player[i], team[i], cost[i]/10)#, position[i]# points[i], utilization[i], minutes[i], cop[i])

#for v in m.getVars():
#	print(v.VarName, v.x)

print('Obj:', m.Objval)

var_series = pd.Series(variables)
var_series.to_csv('~/fantasy-RL/optimal_starting_team_1819.csv')

