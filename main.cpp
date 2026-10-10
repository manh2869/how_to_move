#include <string>
#include <vector>
#include <SFML/Graphics.hpp>
#include <iostream>

using namespace std;
using namespace sf;

int main()
{
    RenderWindow window(
        VideoMode({1000, 700}),
        "move_like_move");
    window.setFramerateLimit(120);
    Clock clock;

    CircleShape circle(60.f);

    circle.setFillColor(Color::Green);

    Vector2 pos = {300.0f, 300.0f};
    Vector2 veclocity = {100.0f, 100.0f};

    vector<CircleShape *> c;

    float speed = 200;

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
            CircleShape *item = new CircleShape(60.0f);
            item->setFillColor(Color::Red);
            item->setPosition(pos);
            c.push_back(item);
            veclocity.x = -veclocity.x;
        }
        if (pos.y <= 0 || pos.y >= 700 - 2 * 60)
        {
            CircleShape *item = new CircleShape(60.0f);
            item->setFillColor(Color::Red);
            item->setPosition(pos);
            veclocity.y = -veclocity.y;
            c.push_back(item);
        }
        window.clear(Color::White);
        for (CircleShape *i : c)
        {
            window.draw(*i);
        }

        pos.x += veclocity.x * dt;
        pos.y += veclocity.y * dt;

        circle.setPosition(pos);
        window.draw(circle);
        window.display();
    }

    return 0;
}
