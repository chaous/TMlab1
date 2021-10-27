import numpy as np
import pygame
import sympy as sp
from sympy.abc import t
from sympy import lambdify





WIDTH, HEIGHT = 1000, 900
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First lab")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
FPS = 60
MULTILIER = 500




def draw(cordinates, i, start, end, start_a, end_a):
    WIN.fill(WHITE)

    pygame.draw.lines(WIN, RED, False, cordinates, 2)
    pygame.draw.circle(WIN, center=(cordinates[i][0], cordinates[i][1]), radius=10, color=BLACK)
    pygame.draw.line(WIN, BLACK, start_pos=start, end_pos=end, width=2)
    pygame.draw.line(WIN, YELLOW, start_pos=start_a, end_pos=end_a, width=2)
    #pygame.draw.line(WIN, CYAN, start_pos=start_r, end_pos=end_r)
    pygame.display.update()




def main(x_cordinates, y_cordinates, x_velocity, y_velocity, x_acceleration_cordinates, y_acceleration_cordinates):
    clock = pygame.time.Clock()
    run = True
    cordinates = []
    for i in range(len(x_cordinates)):
        cordinates.append([x_cordinates[i], y_cordinates[i]])
    #cordinates = cordinates * 1000
    #draw(cordinates)
    i = 0
    while run:
        if i >= len(cordinates):
            i = 0
        #velocity = (x_velocity[i] ** 2 * y_velocity[i]**2) ** 0.5 * MULTILIER
        #print(velocity)
        angle = np.arctan2(x_velocity[i], y_velocity[i])
        #r_curvature = 0.0
        #if x_acceleration_cordinates[i] == y_acceleration_cordinates[i] == 0:
        #    r_curvature = 4000
        #else:
         #   r_curvature = np.sqrt(x_cordinates[i] ** 2 + y_cordinates[i] ** 2) ** 2 / (np.sqrt(x_acceleration_cordinates[i] ** 2
        #                                                                                       + y_acceleration_cordinates[i] ** 2))
        #start_r = [cordinates[i][0], cordinates[i][1]]
        #end_r = [cordinates[i][0] + r_curvature * np.cos(angle), cordinates[i][1] + r_curvature * np.sin(angle)]
        start_v = [cordinates[i][0], cordinates[i][1]]
        end_v = [(cordinates[i][0] + x_velocity[i]), (cordinates[i][1] + y_velocity[i])]
        start_a = start_v
        end_a = [(cordinates[i][0] + x_acceleration_cordinates[i]), (cordinates[i][1] + y_acceleration_cordinates[i])]
        clock.tick(FPS)
        draw(cordinates, i, start_v, end_v, start_a, end_a)
        #print(start, end)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        i += 1








'''dots = np.linspace(0, 100, 10000)
r_from_t = sp.simplify(input("equation for radius vector "))
f_r = np.vectorize(lambdify(t, r_from_t))
#print(f(np.linspace(0, 10, 100)))
r_diff = sp.diff(r_from_t, t)
x_velocity_f = np.vectorize(lambdify(t, r_diff))
#velocity = x_velocity_f(dots)
phi_from_t = sp.simplify(input("equation for angle "))
f_phi = np.vectorize(lambdify(t, phi_from_t))
x_cordinates = np.cos(f_phi(dots)) * f_r(dots)
x_cordinates = MULTILIER * x_cordinates
y_cordinates = np.sin(f_phi(dots)) * f_r(dots)
y_cordinates = MULTILIER * y_cordinates
#plt.plot(x_cordinates, y_cordinates)
#plt.show()
phi_diff = sp.diff(phi_from_t, t)
y_velocity_f = np.vectorize(lambdify(t, phi_diff))
y_velocity = x_velocity_f(dots) * np.sin(y_velocity_f(dots))
x_velocity = x_velocity_f(dots) * np.cos(y_velocity_f(dots))'''


dots = np.linspace(0, 100, 10000)
r_from_t = sp.simplify(input("equation for radius vector "))
#f_r = np.vectorize(lambdify(t, r_from_t))
phi_from_t = sp.simplify(input("equation for angle "))
#f_phi = np.vectorize(lambdify(t, phi_from_t))
x_movement = sp.cos(phi_from_t) * r_from_t
y_movement = sp.sin(phi_from_t) * r_from_t
x_velocity = sp.diff(x_movement, t)
x_acceleration = sp.diff(x_velocity, t)
x_acceleration = np.vectorize(lambdify(t, x_acceleration))
y_velocity = sp.diff(y_movement, t)
avarage_velocity = sp.sqrt(x_velocity**2 + y_velocity**2)
tan_acceleration = sp.diff(avarage_velocity, t)
tan_acceleration = np.vectorize(lambdify(t, tan_acceleration))

x_velocity = np.vectorize(lambdify(t, x_velocity))
y_acceleration = sp.diff(y_velocity, t)
y_acceleration = np.vectorize(lambdify(t, y_acceleration))
y_velocity = np.vectorize(lambdify(t, y_velocity))
x_movement = np.vectorize(lambdify(t, x_movement))
y_movement = np.vectorize(lambdify(t, y_movement))
x_cordinates = x_movement(dots) * MULTILIER
y_cordinates = y_movement(dots) * MULTILIER
x_velocity_cordinates = x_velocity(dots) * MULTILIER
y_velocity_cordinates = y_velocity(dots) * MULTILIER
x_acceleration_cordinates = x_acceleration(dots) * MULTILIER
y_acceleration_cordinates = y_acceleration(dots) * MULTILIER
#acceleration_avarage = np.sqrt(x_acceleration_cordinates**2 + y_acceleration_cordinates**2)
#r_curvature = np.sqrt((x_velocity_cordinates ** 2) + (y_velocity_cordinates ** 2)) / (np.sqrt(acceleration_avarage - tan_acceleration(dots) * MULTILIER))
#print(np.max(r_curvature))





#print(r_from_t.evalf(subs={t: 3.14}))
if __name__ == '__main__':
    main(x_cordinates + CENTER_X, y_cordinates + CENTER_Y, x_velocity_cordinates, y_velocity_cordinates
         , x_acceleration_cordinates, y_acceleration_cordinates)
