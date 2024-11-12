import matplotlib.pyplot as plt
import numpy as np

# Входные данные
m = 3
R = 5
a = np.pi / 2 + np.pi / 6
mu = 0.04

g = 9.81


def velocity_before_ring():
    """
    Определение начальной скорости для прохождения дуги.
    """

    work_against_friction = mu * m * g * R * a
    potential_energy = m * g * R * (1 - np.cos(a))
    required_energy = work_against_friction + potential_energy

    v_initial = np.sqrt(2 * required_energy / m)
    return v_initial


def acceleration_phase():
    """
    Построение разгона до входа на кольцо.
    """

    plt.plot([-2 * R, 0], [0, 0], color='c', label='Разгон до кольца')


def extra_dots():
    """
    Построение доп информации.
    """

    plt.plot([0, 0], [R, 0], linestyle='-.', color='gray')
    plt.plot([0, R * np.sin(a)], [R, R * np.cos(a) + 2 * R], linestyle='-.', color='gray')


def draw_circle():
    """
    Рисование окружности для визуализации кольца.
    """
    theta = np.linspace(0, 2 * np.pi, 1000)
    x_circle = R * np.cos(theta)
    y_circle = R * np.sin(theta) + R
    plt.plot(x_circle, y_circle, linestyle='--', color='gray', label='Дуга')


def motion_on_ring(v_initial):
    """
    Моделирование движения тела по дуге кольца.
    """
    theta = np.linspace(0, a, 1000)
    # theta = np.linspace(0, a, 100)
    friction_force = mu * m * g

    x_ring = []
    y_ring = []
    v_on_ring = v_initial
    for dtheta in theta:
        dv = -friction_force * R * (a / len(theta)) / (m * v_on_ring)
        # dv = -friction_force * R * a / (m * v_on_ring)
        v_on_ring += dv
        x_ring.append(R * np.sin(dtheta))
        y_ring.append(R * (1 - np.cos(dtheta)))

    plt.plot(x_ring, y_ring, color='b', label='Траектория на дуге')
    return v_on_ring, x_ring[-1], y_ring[-1]


def trajectory_after_ring(v_on_ring, x_start, y_start):
    """
    Построение траектории тела после отрыва от кольца.
    """
    # Угловая скорость после отрыва
    v_x = v_on_ring * np.cos(a)
    v_y = v_on_ring * np.sin(a)

    # Время полета после отрыва
    t_flight = (v_y + np.sqrt(v_y ** 2 + 2 * g * y_start)) / g
    t = np.linspace(0, t_flight, 100)

    # Координаты полета
    x = x_start + v_x * t
    y = y_start + v_y * t - 0.5 * g * t ** 2

    plt.plot(x, y, color='y', label='Траектория движения тела')
    plt.scatter([x_start], [y_start], marker='x', color='r', label='Точка отрыва')

    return v_x, v_y, x[-1], y[-1]


def show_results():
    plt.xlabel('x, м')
    plt.ylabel('y, м')
    plt.title('Траектория движения тела')
    plt.axis('equal')
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()


v_initial = velocity_before_ring()
print('Скорость тела, необходимую для прохождения всей длины дуги =', v_initial)
draw_circle()
acceleration_phase()
extra_dots()
v_on_ring, x_start, y_start = motion_on_ring(v_initial)
v_x, v_y, x_end, y_end = trajectory_after_ring(v_on_ring, x_start, y_start)
show_results()
