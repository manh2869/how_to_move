#include <SFML/Graphics.hpp>
#include <iostream>
#include <cmath>

using namespace std;
using namespace sf;

const float gravity = 980;
const float elastic = 0.75;
const float speed = 200;

int main()
{
    RenderWindow window(VideoMode({1000, 700}), "stick man");
    Clock clock;
    window.setFramerateLimit(120);

    float radius = 25.0f;
    float length = 300.f;
    float angle = 0.0f;
    float angularVelocity = 0.0f;

    CircleShape circle(radius);
    RectangleShape rec({5.0f, 300.0f});

    circle.setFillColor(Color::Green);
    rec.setFillColor(Color::Red);

    Vector2f pivot = {500, 50};

    Vector2f pos_rec = {300, 700};
    Vector2f pos_circle = {300, 300};

    rec.setOrigin({2.5, 0});
    circle.setOrigin({radius, radius});

    while (window.isOpen())
    {
        while (const auto event = window.pollEvent())
        {
            if (event->is<Event::Closed>())
                window.close();
        }
        Vector2i mouse = Mouse::getPosition(window);
        float dt = clock.restart().asSeconds();

        rec.setPosition(pivot);
        angle += 0.01;

        // pos_circle.x = pivot.x + length * sin(angle);
        // pos_circle.y = pivot.y + length * cos(angle);

        float angularAcceleration = -(gravity / length) * sin(angle);
        angularVelocity += angularAcceleration * dt;
        angle += angularVelocity * dt;
        pos_circle = {
            pivot.x + length * sin(angle),
            pivot.y + length * cos(angle)};
        circle.setPosition({pos_circle.x, pos_circle.y});
        rec.setRotation(radians(-angle));

        window.clear(Color::White);

        window.draw(rec);
        window.draw(circle);
        window.display();
    };
}
