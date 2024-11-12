# Моделирование №1

> Вариант 1 №9

![model_1](https://github.com/user-attachments/assets/51655a49-81c2-44c8-895f-162a98e90779)

## Задание

> Тело массой $m$ разгоняется в горизонтальной плоскости и попадает на вертикально расположенный фрагмент кольца (дугу) радиуса $R$ и угловым размером $\alpha$ $(\pi/2 \leq \alpha \leq 3\pi/2)$
> Определить скорость тела, необходимую для прохождения всей длины дуги. Изобразить траекторию тела после отрыва от дуги. Дуга имеет коэффициент трения $\mu$.

| №   | Масса тела $m$, кг | Радиус кольца $R$, м | Угловой размер дуги $a$, рад | Коэффициент трения $\mu$ |
| --- | ------------------ | -------------------- | ---------------------------- | ------------------------ |
| 9   | 3                  | 5                    | $\pi/2 + \pi/6$              | 0.04                     |

## Формулы

1. Работа силы трения на дуге:  
   $$W_{тр} = \mu \cdot m \cdot g \cdot R \cdot \alpha$$

2. Изменение потенциальной энергии:  
   $$\Delta E_{п} = m \cdot g \cdot R \cdot (1 - \cos(\alpha))$$

3. Необходимая энергия для прохождения дуги:  
   $$E*{необх} = W_{тр} + \Delta E*{п}$$

4. Начальная скорость для прохождения дуги:  
   $$v*0 = \sqrt{\frac{2 \cdot E_{необх}}{m}}$$

5. Сила трения на дуге:  
   $$F_{тр} = \mu \cdot m \cdot g$$

6. Вертикальная и горизонтальная составляющие скорости после отрыва:  
   $$v_x = v \cdot \cos(\alpha)$$
   $$v_y = v \cdot \sin(\alpha)$$

7. Время полёта после отрыва:  
   $$t_{полет} = \frac{v_y + \sqrt{v_y^2 + 2 \cdot g \cdot y*{start}}}{g}$$

8. Траектория после отрыва:  
   $$x = x*{start} + v_x \cdot t$$
   $$y = y*{start} + v_y \cdot t - \frac{1}{2} \cdot g \cdot t^2$$

## Выводы

В ходе работы была рассчитана скорость, необходимая для прохождения дуги, и визуализирована траектория движения тела. Рассчитанная начальная скорость для прохождения всей длины дуги составила $v_0 = {v_{initial}}$. Также были построены графики разгона тела, движения по дуге и траектории после отрыва.

Данный отчёт демонстрирует использование численных методов для моделирования движения с учётом силы трения и гравитации, а также показывает возможности Python и библиотеки `matplotlib` для визуализации.