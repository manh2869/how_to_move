#include <string>
#include <vector>
#include <SFML/Graphics.hpp>
#include <iostream>
#include <random>
using namespace std;
using namespace sf;
struct ball
{
    CircleShape shape;
    Color col;
    Vector2f vec;
    Vector2f veclocityb;
    float angle;
};

int main()
{
    RenderWindow window(
        VideoMode({1000, 700}),
        "move_like_move");
    window.setFramerateLimit(120);

    mt19937 gen(8);

    Clock clock;

    CircleShape circle(60.f);

    circle.setFillColor(Color::Green);

    Vector2 pos = {300.0f, 300.0f};
    Vector2 veclocity = {100.0f, 100.0f};

    vector<ball> c;
    float speed = 30;

    while (window.isOpen())
    {
        while (const auto event = window.pollEvent())
        {
            if (event->is<Event::Closed>())
                window.close();
        }
        float dt = clock.restart().asSeconds();

        if (pos.x <= 0 || pos.x >= 1000 - 2 * 60)
        {
            ball balls;
            balls.shape = CircleShape(gen() % 80 + 20);
            balls.vec = {float(gen() % 1000), float(gen() % 700)};
            balls.veclocityb = {float(gen() % 1000), float(gen() % 700)};
            balls.col = Color(gen() % 256, gen() % 256, gen() % 256, gen() % 256);
            balls.angle = gen() % 360 + 1;
            balls.shape.setPosition(balls.vec);
            balls.shape.setFillColor(balls.col);
            c.push_back(balls);
            veclocity.x = -veclocity.x;
        }
        if (pos.y <= 0 || pos.y >= 700 - 2 * 60)
        {
            ball balls;
            balls.shape = CircleShape(gen() % 80 + 20);
            balls.vec = {float(gen() % 1000), float(gen() % 700)};
            balls.veclocityb = {float(gen() % 1000), float(gen() % 700)};
            balls.col = Color(gen() % 256, gen() % 256, gen() % 256, gen() % 256);
            balls.angle = gen() % 360 + 1;
            balls.shape.setPosition(balls.vec);
            balls.shape.setFillColor(balls.col);
            c.push_back(balls);
            veclocity.y = -veclocity.y;
        }
        window.clear(Color::White);
        for (ball &b : c)
        {
            b.shape.setFillColor(b.col);
            window.draw(b.shape);
            if (b.shape.getPosition().x <= 0 || b.shape.getPosition().x >= 1000 - 2 * b.shape.getRadius())
            {
                b.veclocityb.x = -b.veclocityb.x;
            }
            if (b.shape.getPosition().y <= 0 || b.shape.getPosition().y >= 700 - 2 * b.shape.getRadius())
            {
                b.veclocityb.y = -b.veclocityb.y;
            }

            b.vec.x += b.veclocityb.x * dt * speed * cos(M_PI / 180 * int(b.angle));
            b.vec.y += b.veclocityb.y * dt * speed * sin(M_PI / 180 * int(b.angle));
            b.shape.setPosition(b.vec);
        }

        pos.x += veclocity.x * dt * speed * cos(M_PI / 180 * 40);
        pos.y += veclocity.y * dt * speed * sin(M_PI / 180 * 40);

        circle.setPosition(pos);
        window.draw(circle);
        window.display();
    }

    return 0;
}
