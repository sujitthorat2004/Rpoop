#include<stdio.h>
#include<stdlib.h>
void main(){
    float tank_depth=0, tank_width=0, tank_length=0, tank_vel=0;
    float popu, demand, deten_period, flow_vel, sludge_depth, free_board;
    int d;
    
    printf("Enter population: ");
    scanf("%f", &popu);
    printf("Enter per capita demand: ");
    scanf("%f", &demand);
    printf("Enter detention period(in hrs): ");
    scanf("%f", &deten_period);
    printf("Enter flow velocity(m/min)\n(between 0.15 to 0.9) ");
    scanf("%f", &flow_vel);
    printf("Do you want to enter sludge-depth and free-board? (1 or 0)");
    scanf("%d", &d);
    if(d==1){
        printf("Enter the sludge-depth and free-board: ");
        scanf("%f %f", &sludge_depth, &free_board);
    }
    else{
        sludge_depth = 0.5;
        free_board = 0.5;
    }
    
    
    float peak_demand = demand * popu * 1.5;
    float avg_demand = popu * demand;
    
    float vol = (deten_period * (peak_demand / 1000)) / 24;
    
    tank_length = deten_period * 60 * flow_vel;
    
    tank_width = tank_length / 6;
    
    tank_depth = vol / (tank_length * tank_width);
    
    float overall_depth = free_board + sludge_depth + tank_depth;
    
    printf("The volume of tank: %f m^3\n", vol);
    printf("The length of tank: %fm\n", tank_length);
    printf("The width of tank: %fm\n", tank_width);
    printf("The depth of tank: %fm\n", tank_depth);
    printf("The overall depth of tank: %f m\n", overall_depth);
    
    
    
    
    
    
    
    
    return;
}